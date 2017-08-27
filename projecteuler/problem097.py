#coding: utf-8

def problem097():
    ltd = '28433' # last ten digits
    for i in range(7830457):
        if len(ltd) > 10:
            ltd = ltd[len(ltd)-10:]
        ltd = str(int(ltd) * 2)
    print int(ltd)+1

if __name__ == '__main__':
    problem097()
