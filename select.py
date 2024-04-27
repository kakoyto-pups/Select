import webbrowser
from PIL import Image

def open_image(image_path):
    image = Image.open(image_path)
    image.show()

def action_1():
    print("Запуск ядерки...")
    open_image('yaderka.webp')

def action_2():
    print("Отображение картинки с не очень богатыми людьми...")
    open_image('bomshi.jpg')

def action_3():
    print("Отображение картинки с ящиком...")
    open_image('box.jpg')

def main_menu():
    print("Выберите действие:")
    print("1 - Запустить ядерку на Новосибирск")
    print("2 - Показать картинку с бомжом")
    print("3 - Показать картинку с красивым ящиком")
    print("0 - Выход")

    choice = input("Введите номер действия: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            action_1()
        elif choice == '2':
            action_2()
        elif choice == '3':
            action_3()
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()