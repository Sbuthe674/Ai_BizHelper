
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Загрузка ключа из .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(f"Значение GEMINI_API_KEY: '{api_key}'")

# Настройка клиента Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("AI-помощник для малого бизнеса")
mode = st.sidebar.selectbox("Выберите режим:", [
    "Генератор постов для соцсетей",
    "Описание продукта",
    "Анализ продаж и прогноз спроса",
    "Ответы на частые вопросы клиентов",
    "Финансовое планирование"
])

if mode == "Генератор постов для соцсетей":
    st.header("Генератор постов")
    product = st.text_input("Введите продукт или услугу")
    tone = st.selectbox("Выберите стиль:", ["Информативный", "Продажный", "Дружелюбный", "Профессиональный"])
    if st.button("Сгенерировать пост"):
        if not product:
            st.warning("Введите продукт или услугу.")
        else:
            prompt = f"Напиши {tone.lower()} пост для Instagram, рекламирующий товар или услугу: {product}"
            response = model.generate_content(prompt)
            st.write(response.text)

elif mode == "Описание продукта":
    st.header("Генератор описаний")
    product = st.text_area("Введите краткое описание товара или услуги")
    if st.button("Сгенерировать описание"):
        if not product:
            st.warning("Введите описание.")
        else:
            prompt = f"Создай профессиональное описание для товара или услуги: {product}"
            response = model.generate_content(prompt)
            st.write(response.text)

elif mode == "Анализ продаж и прогноз спроса":
    st.header("Анализ и прогноз")
    data = st.text_area("Введите данные о продажах (например: товар - количество продаж по месяцам)")
    if st.button("Проанализировать и спрогнозировать"):
        if not data:
            st.warning("Введите данные о продажах.")
        else:
            prompt = f"Проанализируй данные о продажах и сделай прогноз спроса: {data}"
            response = model.generate_content(prompt)
            st.write(response.text)

elif mode == "Ответы на частые вопросы клиентов":
    st.header("Чат-бот для FAQ")
    question = st.text_input("Введите вопрос клиента")
    if st.button("Ответить на вопрос"):
        if not question:
            st.warning("Введите вопрос.")
        else:
            prompt = f"Ответь на вопрос клиента так, как если бы ты был сотрудником малого бизнеса: {question}"
            response = model.generate_content(prompt)
            st.write(response.text)

elif mode == "Финансовое планирование":
    st.header("Финансовый план")
    income = st.text_input("Ожидаемый доход в месяц")
    expenses = st.text_input("Планируемые расходы в месяц")
    goal = st.text_area("Цель (например: накопить на оборудование, открыть новый филиал и т.д.)")
    if st.button("Построить финансовый план"):
        if not income or not expenses or not goal:
            st.warning("Заполните все поля.")
        else:
            prompt = f"Составь простой финансовый план. Доход: {income}, Расходы: {expenses}, Цель: {goal}."
            response = model.generate_content(prompt)
            st.write(response.text)
