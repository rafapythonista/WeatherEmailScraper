WeatherEmailScraper:
Esse projeto é um script em Python que utiliza Selenium para coletar informações de previsão do tempo de um site e depois envia essas informações como um e-mail em formato HTML. Ele faz scraping da página, obtém dados como temperatura e previsão para os próximos dias, e utiliza Jinja2 para gerar o conteúdo do e-mail. Finalmente, o e-mail é enviado através do servidor SMTP do Gmail.

Funcionalidades:

•	Obtenção de dados Utiliza Selenium para cessar o site do tempo.com, inserir a cidade e extrair temperatura atual, condição do tempo e previsão para os próximos 3 dias.
•	Envio por E-mail: Formata os dados obtidos em um e-mail HTML e envia para um destinatário configurado. – Agendamento: Utiliza a biblioteca schedule para agendar a execução diária do script.

Requisitos:

Python 3x Bibliotecas Python necessárias: selenium, webdriver_manager, schedule, smtplib, email, dotenv Conta de e-mail Gmail para envio.

Configuração: 

•	Instale as dependências necessárias: pip install selenium webdriver_manager schedule
•	Execute o script para testar o envio de e-mails: python app.py

Notas: 
Certifique-se de que o Chrome WebDriver está instalado e configurado corretamente.       
