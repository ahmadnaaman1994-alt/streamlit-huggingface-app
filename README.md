# Приложение для анализа тональности (Streamlit + HuggingFace)

Это простое веб-приложение на Streamlit, использующее модель из HuggingFace для определения тональности текста на разных языках (включая русский, английский и арабский).

## Основная идея

Приложение принимает текст от пользователя и определяет его эмоциональную окраску в формате:

1 — очень негативно  
5 — очень позитивно

Используемая модель:
```
nlptown/bert-base-multilingual-uncased-sentiment
```
## Как запустить локально
```
pip install -r requirements.txt
streamlit run app.py
```
## Онлайн-версия приложения

(https://app-huggingface-app-xr6pkvh7ks9dhskghgzavu.streamlit.app/)

## Автор

Нуман Ахмед
