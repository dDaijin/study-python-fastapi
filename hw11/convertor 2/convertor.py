import os
import comtypes.client

def doc_to_pdf(doc_file, pdf_file=None):
    if not pdf_file:
        pdf_file = os.path.splitext(doc_file)[0] + ".pdf"
    
    print(f"Перевірка: намагаємось конвертувати {doc_file} у {pdf_file}")

    try:
        # Створюємо об'єкт для Microsoft Word
        word = comtypes.client.CreateObject('Word.Application')
        
        # Відкриваємо документ
        doc = word.Documents.Open(os.path.abspath(doc_file))
        print(f"Документ {doc_file} відкритий успішно.")
        
        # Зберігаємо як PDF
        doc.SaveAs(os.path.abspath(pdf_file), FileFormat=17)  # 17 - це формат PDF
        doc.Close()
        word.Quit()

        print(f"✅ DOCX успішно конвертовано в PDF: {pdf_file}")
    except Exception as e:
        print(f"Помилка: {e}")
        print("Перевірте наявність Microsoft Word та правильність шляху до файлу.")

if __name__ == "__main__":
    doc_to_pdf("example.docx")  # Замінити на правильне ім'я файлу
