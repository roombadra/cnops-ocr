from pdf2image import convert_from_path
from pytesseract import image_to_string


def get_text_from_any_pdf(pdf_file: str) -> str:
    """
    @desc: this function is our final system combining the previous functions
    @params: file: the original PDF File
    @returns: the textual content of ALL the pages
    """
    images = convert_from_path(pdf_path=pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += image_to_string(img)
    return final_text


def test1():
    """
    @desc: this function call get_text_from_any_pdf and convert the text to list for delete empty line then convert to str
    @remark 1: 'd'offre' line 03 return '@offres', only for this line we need to replace @ by d. It probaly because of the font family
    @remark 2: 'pour: Mise' line 03 return 'pour:Mise', it because 'pour:' and 'Mise' are not the same font family
    @remark 3: 'œuvre' line 03 return 'ceuvre'
    @remark 4 : 'contrôle' line 04 'contrdle'
    @remark 5 : 'fixé à la somme' line 13 return 'fixé 4 la somme'
    @remark 6 : '(20Mars 2023)' line 18 return '(20Mars 20138)'
    @remark 7 : "a l'arrété du Ministére de l’Economie et des Finances n° 20-14 du 08 kaâda" line 23 return "a larrété du Ministére de ’Economie et des Finances n° 20-14 du 08 kadda"
    @remark 8 : 'justificatives à fournir' line 24 return 'justificatives a4 fournir'
    @remark 9 : in the file end we have '} {' it because of the sign at the file end
    :return:
    """
    get_text = get_text_from_any_pdf(
        "/home/roombadra/Téléchargements/AVIS_D_APPEL_D_IOFFRES_OUVERT_N26-2022-DRAFM.pdf")
    text_to_list = get_text.splitlines()
    # delete all of empty line from the list
    text = [line for line in text_to_list if line.strip() != ""]
    text_final = ' '.join([str(elem) for elem in text])
    file = open("text/text.txt", "wt")
    file.write(text_final)
    file.close()
    title = ""


if __name__ == '__main__':
    test1()
