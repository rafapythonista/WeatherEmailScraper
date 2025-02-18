from dotenv import load_dotenv
from jinja2 import Template
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import smtplib
from email.message import EmailMessage
import os
def iniciar_driver():

    load_dotenv()

    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=900,500', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': caminho_padrao_para_download,
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver
# Template HTML com placeholders para os dados dinâmicos
html_template = """
<!doctype html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Previsão Climática</title>
</head>
<body>
    <h1>Previsões Climáticas para Jacareí</h1>
    <p>Atenção! Fique por dentro das previsões climáticas em Jacareí.</p>
    <p><strong>Temperatura atual:</strong> {{ temperatura }}</p>
    <p><strong>Condição atual:</strong>  {{ condicao_weather }}</p>
    <p><strong>Previsão para os próximos 3 dias:</strong> </p>
    <ul>
        {% for previsao in previsoes %}
            <li>{{ previsao.dia }}: {{ previsao.temperatura_max }} - {{ previsao.condicao }} ({{ previsao.temperatura_min }})</li>
        {% endfor %}
    </ul>
    <footer>
        <p>Powered by Dev Twins</p>
    </footer>
</body>
</html>
"""

# Dados dinâmicos a serem passados para o template
temperatura = "28°C"
condicao_weather = "Ensolarado"
previsao_3_dias = [
    {"dia": "Segunda", "temperatura_max": "27°C", "temperatura_min": "20°C", "condicao": "Parcialmente nublado"},
    {"dia": "Terça", "temperatura_max": "29°C", "temperatura_min": "22°C", "condicao": "Ensolarado"},
    {"dia": "Quarta", "temperatura_max": "25°C", "temperatura_min": "18°C", "condicao": "Chuvoso"}
]

# Função principal
def main():
    driver = iniciar_driver()
    driver.get('https://www.tempo.com/jacarei_sao-paulo-l115835.htm')

driver = iniciar_driver()
driver.get('https://www.tempo.com/jacarei_sao-paulo-l115835.htm')

try:
    # Espera até que o elemento contendo a temperatura apareça na página (tempo máximo de 10 segundos)
    temperatura = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.dato-temperatura.changeUnitT'))
    ).text  # Obtém o texto da temperatura

    # Captura a condição do tempo (exemplo: "Ensolarado", "Nublado", etc.)
    condicao_weather = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.descripcion'))
    ).text           

    # Captura os elementos da previsão para os próximos dias
   # Captura os textos dos elementos
    data_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.subtitle-m')]
    previsao_condicao_climatica_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.descripcion')]
    previsao_max_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.max.changeUnitT')]
    previsao_min_text = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, '.min.changeUnitT')]

       # Prepara os dados de previsão para passar ao template
    previsao_3_dias = [
            {"dia": data_text[i], "condicao": previsao_condicao_climatica_text[i], "temperatura_max": previsao_max_text[i], "temperatura_min": previsao_min_text[i]}
            for i in range(3)
        ]

        # Gerar o conteúdo do e-mail com o Jinja2
    template = Template(html_template)
    html_content = template.render(
            temperatura=temperatura,
            condicao_weather=condicao_weather,
            previsoes=previsao_3_dias
        )
    # Configuração do e-mail
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    mail = EmailMessage()
    mail['Subject'] = 'Prepare-se para uma semana de clima instável em Jacareí!'
    mail['From'] = EMAIL_ADDRESS
    mail['To'] = 'rafaelmirandadevv@gmail.com'
    mail.set_content(html_content, subtype='html')  # Define o conteúdo do e-mail (em texto simples)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email.send_message(mail)

    print('E-mail enviado com sucesso!')
    
except Exception as e:
    print(f'Erro ao obter a temperatura ou enviar o e-mail: {e}')
finally:






    driver.quit()

input('Pressione Enter para sair...')






