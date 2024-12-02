from mistralai import Mistral
from config import AI_TOKEN
async def generate(age, experience, level, goal, type_tr, quantity, zones):
    s = Mistral(
        api_key=AI_TOKEN,
    )
    res = await s.chat.complete_async(model="mistral-small-latest", messages=[
        {
            "content": f'Составь программу тренировок по следующим входным данным: Ты должен составить эту программу для человека возраста {age}, опыт занятия в зале составляет {experience}, его уровень физичиеской подготовки - {level}, основная цель его занятий - {goal}, предпочтительный тип тренировок - {type_tr} он готов ходить в зал {quantity} раз в неделю, один раз в неделю добавь одно упражнение на следующую зону: {zones}. Ответ напищи на русском языке. Вступительной фразой должна быть: "Вот ваша программа тренировок". Больше ничего вступительного писать не нужно. Количество тренировочных дней обязательно должно совпадать с введеным',
            "role": "user",
        },
    ])
    if res is not None:
        return res.choices[0].message.content
