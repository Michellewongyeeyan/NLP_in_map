<h1 align="center"><b>NLP_in_map</b></h1>

<main style="text-align: center;">
這項目的目標是產生一個 Web 應用程序，允許使用者繪製文本中提到的地點的地圖。
該系統將使用命名實體識別 (NER) 和地理編碼軟體（例如 SpaCy 和 GeoPy 庫分別提供的軟體）來識別和地理編碼（產生座標）使用者提供的文本中提到的位置。
然後，這些位置將被繪製在地圖上（使用背景地圖，例如 OpenStreetMap 的背景地圖）。
</main>

<br/>

> 根據進展情況，系統的更高級版本可以維護一個可以在地圖上進行比較的使用者文字庫。
> 進一步的進展可以提供文字的空間索引，以便對於給定區域，可以檢索和顯示所有相關文字。


# 目標
1. 用Spacy Detect嘅內容
2.  想整一個Web比一啲對Ulysses呢本書有興趣嘅人用嘅，特別係想研究本書裏面提及咗咩地點嘅人

1. 優化NLP Model，拎曬啲地名地理位置出泥。
2. 係Web到show個地圖出泥，地圖畫曬地名地方出泥。
3. user可以按佢，就到書文字上對應位置？

# 技術
python 
- scipy
- SpaCy / GeoPy

# link
https://idp.cf.ac.uk/idp/profile/SAML2/Redirect/SSO?execution=e1s1
https://wiki.openstreetmap.org/wiki/Overpass_API
https://www.openstreetmap.org/#map=19/22.35805/114.12968
