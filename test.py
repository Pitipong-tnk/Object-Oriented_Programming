import requests
import html

# ดึงข้อมูลจาก API
url = 'https://opentdb.com/api.php?amount=10'
result = requests.get(url).json()

# ตรวจสอบว่า API ส่งข้อมูลสำเร็จ
if result['response_code'] == 0:  # 0 หมายถึงข้อมูลถูกส่งสำเร็จ
    questions = result['results']
    for i, question in enumerate(questions, start=1):
        # แปลงอักขระ HTML ให้อยู่ในรูปแบบที่อ่านได้
        question_text = html.unescape(question['question'])
        correct_answer = html.unescape(question['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in question['incorrect_answers']]
        
        # แสดงคำถาม
        print(f"Question {i}: {question_text}")
        print("Options:")
        
        # รวมคำตอบที่ถูกและผิด แล้วสลับตำแหน่งแบบสุ่ม
        options = incorrect_answers + [correct_answer]
        for j, option in enumerate(options, start=1):
            print(f"  {j}. {option}")
        
        # แสดงคำตอบที่ถูกต้อง
        print(f"Answer: {correct_answer}")
        print("\n")
else:
    print("Failed to fetch questions.")
