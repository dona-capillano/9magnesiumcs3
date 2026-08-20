# Chinese Zodiac sign Finder
**Name:** Dona
**Section:** Magnesium
**School Year:** 2026-2027
## Requirements
- Ask user to enter a year of birth (baseline year: 1900)
- Validate input so it is not earlier than 1900
- If the year is invalid, display an error message.
- Otherwise, determine the Chinese Zodiac sign based on a 12-year cycle
- Consider only the year of birth

---
## python Code ('zodiacMagnesiumCapillano.py')
'''python
zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

baseline_year = 1900
birth_year = int(input("Enter your birth year: "))
if birth_year < baseline_year:
    print("Inalid year, it shouldn't be earlier than 1900")
else: 
    index = (birth_year - baseline_year) % 12
    print (f"Your Chinese zodiac Sign is: {zodiac_signs[index]}")
