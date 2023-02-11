<div style ="font-family:Courier New, monospace">

<ins><h1 align="center">KANDİLLİ RASATHANE API</h1></ins>
 <div style = "font-size: 100%">
 {Tr}Kandilli Rasathanesinin yayınladığı son 500 deprem hakkında dilediğiniz depremi sorgulayabilir, canlı olarak uygulamalarınızda gösterebilirsiniz.
 </div>
 <br>
<div style = "font-size: 100%">
 {Eng}You can query any earthquake you want about the last 500 earthquakes published by the Kandilli Observatory and show them live in your applications.
</div>
<br><br>

<ins><h1 align="center">EndPoints</h1></ins>
<div align="center", style="font-size:150%">
    Url = https://deprem-api-delta.vercel.app/
</div>
<br><br><br>
<ins><h1 align="center">{Tr}Neler yapabilir ?<br>//<br>{Eng}What it can do ?</h1></ins>
    <div align="center", style="font-size:150%">{Tr}</div>
    <div align="center", style="font-size:100%">
1->Son 500 depremi görebilir. <br>
2->Dilediğiniz ilk x kadar depremi gösterebilir. <br>
3->Dilediğiniz son x kadar depremi gösterebilir.<br>
4->Son depremi gösterebilir.<br>
5->İlk depremi gösterebilir.<br>
6->Seçtiğiniz tarihteki depremleri gösterebilir. <br>
7->Seçtiğiniz tarihte olan x kadar depremi gösterebilir.<br>
8->Seçtiğiniz tarihler arasındaki depremleri gösterebilir.<br>
9->Seçtiğiniz tarihler arasındaki x kadar depremi gösterebilir.<br>
</div>
<div>
not: Rasathane sayfasındaki en üstteki veri api için "ilk",
Rasathane sayfasındaki en alttaki veri api için "son"dur.
</div>
<br>
<div align="center", style="font-size:150%">
{Eng}
</div>
<div align="center", style="font-size:100%">
1->It can see the last 500 earthquakes.<br> 
2->It can show you the first x number of earthquakes. <br>
3->It can show you the last x number of earthquakes. <br>
4->It can show the last earthquake.<br>
5->It can show the first earthquake. <br>
6->It can show earthquakes on the date you choose. <br>
7->Can show up to x number of earthquakes on the date you select<br>
8->It can show earthquakes between the dates you choose. <br>
9->It can show x number of earthquakes between the dates you select.<br>
</div>
<div>
note: The top data on the Observatory page is "first" for the api,
The bottom data on the observatory page is "last" for the api.
</div>
<br><br>
<ins><h1 align="center"> {Tr}ÖNEMLİ NOT <br>//<br> {Eng}IMPORTANT NOTE</h1></ins>
<div align="center", style= "font-size:100%">
{Tr}Ticari amaçlar için lütfen boğaziçi rasathanesinden izin alınız.
<br>
{Eng}For commercial purposes, please obtain permission from the Boğaziçi Observatory.
</div>
<br><br>
<ins><h1 align="center">{Tr}Peki nasıl ?<br>//<br>{Eng}So how ?</h1></ins>
<div style = "font-size:100%;">
    <div align="center", style="font-size:85%">
    {Tr}<br>
    1->500 Depreme bakma = /tum<br>
    2->İlk x depremi gösterme = /ilk/x<br>
    3->Son x depremi gösterme = /son/x<br>
    4->Son depremi gösterme = /son<br>
    5->İlk depremi gösterme = /ilk<br>
    6->Seçtiğiniz tarihteki depremleri gösterme = /tum/YYYY.MM.DD<br>
    7->Seçtiğiniz tarihteki x kadar depremleri gösterme = /tum/YYYY.MM.DD/x <br>
    8->Seçtiğiniz tarihler arasındaki depremleri gösterme = /tum/YYYY.MM.DD-YYYY.MM.DD <br>
    9->Seçtiğiniz tarihler arasındaki x kadar depremi gösterme = /tum/YYYY.MM.DD-YYYY.MM.DD-x<br>
    Önemli : Dönüşler Json(dict) şeklindedir.
    <br>
    <br>
    </div>
    <div align="center", style="font-size:85%">
    {Eng}<br>
    1->Displaying 500 earthquakes = /tum<br>
    2->Displaying the first x earthquakes = /ilk/x<br>
    3->Displaying the last x earthquakes = /son/x<br>
    4->Displaying last earthquakes = /son<br>
    5->Displaying first earthquakes = /ilk<br>
    6->Displaying earthquakes on the date of your choice = /tum/YYYYY.MM.DD<br>
    7->Displaying x earthquakes on the date of your choice = /tum/YYYYY.MM.DD/x<br>
    8->Displaying earthquakes between your selected dates = /tum/YYYYYY.MM.DD-YYYYYY.MM.DD<br>
    9->Displaying x number of earthquakes between selected dates = /tum/YYYYYY.MM.DD-YYYYYY.MM.DD-x <br>
    Important : Important : Returns are in Json(dict).
    </div>
</div>
<br><br>
<ins><h1 align="center">İletişim <br>//<br> Contact</h1></ins>
<lu align="center">
<h3>{Tr}Sorular ve İstekler için --></h3>
<li>Mail adresi : ertugrulmutlu004@gmail.com</li>
</lu>
<br>
<lu align="center">
<h3>{Eng}For Questions and Requests --></h3>
<li>Mail adress : ertugrulmutlu004@gmail.com</li>
</lu>
</div>
