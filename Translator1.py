from googletrans import Translator, LANGUAGES

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def main():
    print("Welcome to the Language Translator!")
    print("Available languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

    text = input("Enter the text you want to translate: ")
    dest_language = input("Enter the language code you want to translate to (e.g., 'fr' for French): ")

    if dest_language in LANGUAGES:
        translated_text = translate_text(text, dest_language)
        print(f"Translated text: {translated_text}")
    else:
        print("Invalid language code. Please try again.")

if __name__ == "__main__":
    main()