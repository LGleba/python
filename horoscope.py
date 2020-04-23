# 2020
# Horoscope from ignio.com + Parser XML for ignio.com + Language Horoscope: Russian
# Powered by LGleba


import requests


def makeMatrixHoroscope():
    url = "https://ignio.com/r/export/win/xml/daily/com.xml"
    response = requests.get(url)
    s = response.text
    text = s.split('\n\n')
    text = text[1:-2]

    # Creating matrix
    matrixHoroscope = [False] * 12
    for i in range(12):
        matrixHoroscope[i] = [False] * 3

    # Form matrix horoscope
    for i in range(len(text)):
        temp = text[i].split('\n')
        matrixHoroscope[i][0] = temp[2]
        matrixHoroscope[i][1] = temp[5]
        matrixHoroscope[i][2] = temp[8]
    return matrixHoroscope

""" Example
if requestOne == "aries" and requestTwo == "yesterday":
    return MatrixHoroscope[0][0]
elif requestOne == "aries" and requestTwo == "today":
    return MatrixHoroscope[0][1]
elif requestOne == "aries" and requestTwo == "tomorrow":
    return MatrixHoroscope[0][2]

elif requestOne == "taurus" and requestTwo == "yesterday":
    return MatrixHoroscope[1][0]
elif requestOne == "taurus" and requestTwo == "today":
    return MatrixHoroscope[1][1]
elif requestOne == "taurus" and requestTwo == "tomorrow":
    return MatrixHoroscope[1][2]

elif requestOne == "gemini" and requestTwo == "yesterday":
    return MatrixHoroscope[2][0]
elif requestOne == "gemini" and requestTwo == "today":
    return MatrixHoroscope[2][1]
elif requestOne == "gemini" and requestTwo == "tomorrow":
    return MatrixHoroscope[2][2]

elif requestOne == "cancer" and requestTwo == "yesterday":
    return MatrixHoroscope[3][0]
elif requestOne == "cancer" and requestTwo == "today":
    return MatrixHoroscope[3][1]
elif requestOne == "cancer" and requestTwo == "tomorrow":
    return MatrixHoroscope[3][2]

elif requestOne == "leo" and requestTwo == "yesterday":
    return MatrixHoroscope[4][0]
elif requestOne == "leo" and requestTwo == "today":
    return MatrixHoroscope[4][1]
elif requestOne == "leo" and requestTwo == "tomorrow":
    return MatrixHoroscope[4][2]

elif requestOne == "virgo" and requestTwo == "yesterday":
    return MatrixHoroscope[5][0]
elif requestOne == "virgo" and requestTwo == "today":
    return MatrixHoroscope[5][1]
elif requestOne == "virgo" and requestTwo == "tomorrow":
    return MatrixHoroscope[5][2]

elif requestOne == "libra" and requestTwo == "yesterday":
    return MatrixHoroscope[6][0]
elif requestOne == "libra" and requestTwo == "today":
    return MatrixHoroscope[6][1]
elif requestOne == "libra" and requestTwo == "tomorrow":
    return MatrixHoroscope[6][2]

elif requestOne == "scorpio" and requestTwo == "yesterday":
    return MatrixHoroscope[7][0]
elif requestOne == "scorpio" and requestTwo == "today":
    return MatrixHoroscope[7][1]
elif requestOne == "scorpio" and requestTwo == "tomorrow":
    return MatrixHoroscope[7][2]

elif requestOne == "sagittarius" and requestTwo == "yesterday":
    return MatrixHoroscope[8][0]
elif requestOne == "sagittarius" and requestTwo == "today":
    return MatrixHoroscope[8][1]
elif requestOne == "sagittarius" and requestTwo == "tomorrow":
    return MatrixHoroscope[8][2]

elif requestOne == "capricorn" and requestTwo == "yesterday":
    return MatrixHoroscope[9][0]
elif requestOne == "capricorn" and requestTwo == "today":
    return MatrixHoroscope[9][1]
elif requestOne == "capricorn" and requestTwo == "tomorrow":
    return MatrixHoroscope[9][2]

elif requestOne == "aquarius" and requestTwo == "yesterday":
    return MatrixHoroscope[10][0]
elif requestOne == "aquarius" and requestTwo == "today":
    return MatrixHoroscope[10][1]
elif requestOne == "aquarius" and requestTwo == "tomorrow":
    return MatrixHoroscope[10][2]

elif requestOne == "pisces" and requestTwo == "yesterday":
    return MatrixHoroscope[11][0]
elif requestOne == "pisces" and requestTwo == "today":
    return MatrixHoroscope[11][1]
elif requestOne == "pisces" and requestTwo == "tomorrow":
    return MatrixHoroscope[11][2]
else:
    return "Error!"
"""
