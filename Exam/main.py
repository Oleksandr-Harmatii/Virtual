# main.py

def reverse_string(s: str) -> str:
    """
    Функція приймає рядок 's' та повертає цей рядок у зворотному порядку.
    """
    return s[::-1]

if __name__ == "__main__":
    # Приклад використання функції.
    input_str = "Hello, World!"
    print(f"Оригінальний рядок: {input_str}")
    print(f"Обернений рядок: {reverse_string(input_str)}")
