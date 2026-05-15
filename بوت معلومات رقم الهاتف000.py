import telebot
from telebot import types
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

API_TOKEN = input('Token : ')
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    chaneel_button = types.InlineKeyboardButton("قناتنا على التيلجرام", url=f"https://t.me/ali313eme")
    markup.add(chaneel_button)
    bot.send_message(message.chat.id, 'أهلاً!\n أرسل لي رقم الهاتف بصيقه دوليه لتحصل على المعلومات.', reply_markup=markup)
    chaneel_button = types.InlineKeyboardButton("قناتنا على التيلجرام", url=f"https://t.me/ali313eme")
@bot.message_handler(func=lambda message: True)
def infonumber(message):
    User_phone = message.text.strip()
    default_region = "2104587940"
    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        response = (
            f"Location             : {location}\n"
            f"Region Code          : {region_code}\n"
            f"Timezone             : {timezoneF}\n"
            f"Operator             : {jenis_provider}\n"
            f"Valid number         : {is_valid_number}\n"
            f"Possible number      : {is_possible_number}\n"
            f"International format : {formatted_number}\n"
            f"Mobile format        : {formatted_number_for_mobile}\n"
            f"Original number      : {parsed_number.national_number}\n"
            f"E.164 format         : {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}\n"
            f"Country code         : {parsed_number.country_code}\n"
            f"Local number         : {parsed_number.national_number}\n"
        )

        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            response += "Type                 : This is a mobile number"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            response += "Type                 : This is a fixed-line number"
        else:
            response += "Type                 : This is another type of number"

        # إنشاء الأزرار
        markup = types.InlineKeyboardMarkup()
        whatsapp_button = types.InlineKeyboardButton("حسابه في واتساب", url=f"https://wa.me/{parsed_number.national_number}")
        telegram_button = types.InlineKeyboardButton("حسابه في تيلجرام", url=f"https://t.me/{User_phone}")
        
        markup.add(whatsapp_button, telegram_button)
        bot.send_message(message.chat.id, response, reply_markup=markup)
    except phonenumbers.NumberParseException:
        bot.reply_to(message, "رقم الهاتف غير صالح. تأكد من إدخاله بشكل صحيح.")

if __name__ == '__main__':
    bot.polling()
    #تخمط اذكر المصدر