"""Auto-generated file, do not edit by hand. AX metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AX = PhoneMetadata(id='AX', country_code=358, international_prefix='00|99[049]',
    general_desc=PhoneNumberDesc(national_number_pattern='[135]\\d{5,9}|[27]\\d{4,9}|4\\d{5,10}|6\\d{7,8}|8\\d{6,9}', possible_number_pattern='\\d{5,12}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='18[1-8]\\d{3,9}', possible_number_pattern='\\d{6,12}', example_number='1812345678'),
    mobile=PhoneNumberDesc(national_number_pattern='4\\d{5,10}|50\\d{4,8}', possible_number_pattern='\\d{6,11}', example_number='412345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{4,7}', possible_number_pattern='\\d{7,10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='[67]00\\d{5,6}', possible_number_pattern='\\d{8,9}', example_number='600123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='10[1-9]\\d{3,7}|2(?:0(?:[16-8]\\d{3,7}|2[14-9]\\d{1,6}|[3-5]\\d{2,7}|9[0-7]\\d{1,6})|9\\d{4,8})|30[1-9]\\d{3,7}|7(?:1\\d{7}|3\\d{8}|5[03-9]\\d{2,7})', possible_number_pattern='\\d{5,10}', example_number='10112345'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0')
