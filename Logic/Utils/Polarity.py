import json
import os
import configparser
from watson_developer_cloud import AlchemyLanguageV1


class Bluemix:
    """
        :Date: 2016-12-12
        :Version: 0.1
        :Author: Juan Camilo Campos - Pontificia Universidad Javeriana Cali
        :Copyright: To be defined
        :Organization: Centro de Excelencia y Apropiación de Big Data y Data Analytics - CAOBA

        This class is composed by several methods, that leverages the IBM Bluemix tools to calculate some variables as
         polarity, keywords and language.

    """

    def __init__(self):
        """
        :Date: 2016-12-12
        :Version: 0.1
        :Author: Juan Camilo Campos - Pontificia Universidad Javeriana Cali

        Constructor for the class

        :rtype: object
        :return: Defines the variables of the class
        """

        self.Config = configparser.ConfigParser()
        if os.path.isfile('../Model/Configuration/BluemixConfiguration.config'):
            self.Config.read('../Model/Configuration/BluemixConfiguration.config')
            self.api_key = self.Config.get('AlchemySettings', 'api_key')

    def polarity(self, text):
        """
                :Date: 2016-12-12
                :Version: 0.1
                :Author: Juan Camilo Campos - Pontificia Universidad Javeriana Cali

                :rtype: json
                :return: the json that contains the values obtained from Bluemix (polarity, lang, keywords)

        """

        alchemy_language = AlchemyLanguageV1(api_key=self.api_key)
        combined_operations = ['keyword', 'doc-sentiment']
        json_data = alchemy_language.combined(text=text, extract=combined_operations)

        if json_data['status'] == "OK":
            type = json_data['docSentiment']['type']
            if type == 'neutral':
                name = 'Neutral'
                value = 0.0
            elif type == 'negative':
                name = 'Negativo'
                value = float(json_data['docSentiment']['score'])
            else:
                name = 'Positivo'
                value = float(json_data['docSentiment']['score'])

            try:
                if self.Config.get('LanguageTranslation', json_data["language"]):
                    lang = self.Config.get('LanguageTranslation', json_data["language"])

            except Exception:
                lang = 'otro idioma'

            json_doc = []
            json_inside = {"polarity_name": name, "polarity_value": value, "language": lang}
            json_doc.append(json_inside)

            json_inside = {"keywords": json_data['keywords']}
            json_doc.append(json_inside)

        else:
            json_doc = []
            json_inside = {"polarity_name": str(), "polarity_value": 0.0, "language": str()}
            json_doc.append(json_inside)

            json_inside = {"keywords": list()}
            json_doc.append(json_inside)

        return json.dumps(json_doc)
