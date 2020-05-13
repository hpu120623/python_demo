class TaxMissNoticeDBM(object):
    code = ''
    name = ''
    legal_person = ''
    address = ''
    tax_arrear = ''
    tax_authority = ''
    tax_balance = 0.0
    tax_balance_new = 0.0
    announcement_time = ''
    city_code = 0

f = TaxMissNoticeDBM()
print(dict((name, getattr(f, name)) for name in dir(f) if not name.startswith('__')))