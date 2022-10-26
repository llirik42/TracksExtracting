from src.extractor import Extractor


extractor = Extractor()

extracted_data = extractor.extract(query='system of down')

print(extracted_data)
print()

search_result = extractor.search(query='bmth sempiternal', limit=5, type_='all', source='yandex')
print(search_result)
