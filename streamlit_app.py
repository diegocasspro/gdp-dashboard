import streamlit as st
import pandas as pd
from io import StringIO

# Função para formatar a data no padrão brasileiro
def formatar_data(data):
    return data.strftime('%d/%m/%Y') if data else ''

# Inicializa o estado da aplicação
if 'dados' not in st.session_state:
    st.session_state.dados = []

# Dados dos planos
planos_dados = [
    {"Número do Plano": "1", "Nome do Plano": "GEAPSAÚDE"},
    {"Número do Plano": "2", "Nome do Plano": "GEAPFAMILIA"},
    {"Número do Plano": "3", "Nome do Plano": "GEAPESSENCIAL"},
    {"Número do Plano": "4", "Nome do Plano": "GEAPESSENCIAL AGREGADOS"},
    {"Número do Plano": "5", "Nome do Plano": "GEAPREFERENCIA"},
    {"Número do Plano": "6", "Nome do Plano": "GEAPREFERENCIA AGREGADOS"},
    {"Número do Plano": "7", "Nome do Plano": "GEAPCLASSICO"},
    {"Número do Plano": "8", "Nome do Plano": "GEAPCLASSICO AGREGADOS"},
    {"Número do Plano": "9", "Nome do Plano": "GEAPSAUDE II"},
    {"Número do Plano": "11", "Nome do Plano": "GEAPSAUDE VIDA"},
    {"Número do Plano": "12", "Nome do Plano": "GEAP SAUDE VIDA GRUPO FAMILIAR"},
    {"Número do Plano": "13", "Nome do Plano": "GEAP REFERENCIA VIDA"},
    {"Número do Plano": "14", "Nome do Plano": "GEAP REFERENCIA VIDA GRUPO FAM"},
    {"Número do Plano": "15", "Nome do Plano": "GEAP Para Você SC"},
    {"Número do Plano": "16", "Nome do Plano": "GEAP Para Você SC Grupo Familiar"},
    {"Número do Plano": "17", "Nome do Plano": "GEAP Para Você DF"},
    {"Número do Plano": "18", "Nome do Plano": "GEAP Para Você DF Grupo Familiar"},
    {"Número do Plano": "19", "Nome do Plano": "GEAP Para Você AM"},
    {"Número do Plano": "20", "Nome do Plano": "GEAP Para Você AM Grupo Familiar"},
    {"Número do Plano": "21", "Nome do Plano": "GEAP Para Você PE"},
    {"Número do Plano": "22", "Nome do Plano": "GEAP Para Você PE Grupo Familiar"},
    {"Número do Plano": "23", "Nome do Plano": "GEAP Para Você ES"},
    {"Número do Plano": "24", "Nome do Plano": "GEAP Para Você ES Grupo Familiar"},
    {"Número do Plano": "25", "Nome do Plano": "GEAP Para Você MG"},
    {"Número do Plano": "26", "Nome do Plano": "GEAP Para Você MG Grupo Familiar"},
    {"Número do Plano": "27", "Nome do Plano": "GEAP Para Você RS"},
    {"Número do Plano": "28", "Nome do Plano": "GEAP Para Você RS Grupo Familiar"},
    {"Número do Plano": "29", "Nome do Plano": "GEAP Para Você GO"},
    {"Número do Plano": "30", "Nome do Plano": "GEAP Para Você GO Grupo Familiar"},
    {"Número do Plano": "31", "Nome do Plano": "GEAP Para Você MS"},
    {"Número do Plano": "32", "Nome do Plano": "GEAP Para Você MS Grupo Familiar"},
    {"Número do Plano": "33", "Nome do Plano": "GEAP Para Você PA"},
    {"Número do Plano": "34", "Nome do Plano": "GEAP Para Você PA Grupo Familiar"},
    {"Número do Plano": "35", "Nome do Plano": "GEAP Para Você PR"},
    {"Número do Plano": "36", "Nome do Plano": "GEAP Para Você PR Grupo Familiar"},
    {"Número do Plano": "37", "Nome do Plano": "GEAP Para Você RJ"},
    {"Número do Plano": "38", "Nome do Plano": "GEAP Para Você RJ Grupo Familiar"},
    {"Número do Plano": "39", "Nome do Plano": "GEAP Para Você MT"},
    {"Número do Plano": "40", "Nome do Plano": "GEAP Para Você MT Grupo Familiar"},
    {"Número do Plano": "41", "Nome do Plano": "GEAP Para Você PB"},
    {"Número do Plano": "42", "Nome do Plano": "GEAP Para Você PB Grupo Familiar"},
    {"Número do Plano": "43", "Nome do Plano": "GEAP BASIC I MG"},
    {"Número do Plano": "44", "Nome do Plano": "GEAP BASIC I MG GRUPO FAMILIAR"},
    {"Número do Plano": "45", "Nome do Plano": "GEAP CLASS II MG"},
    {"Número do Plano": "46", "Nome do Plano": "GEAP CLASS II MG GRUPO FAMILIAR"},
    {"Número do Plano": "47", "Nome do Plano": "GEAP BASIC I PA"},
    {"Número do Plano": "48", "Nome do Plano": "GEAP BASIC I PA GRUPO FAMILIAR"},
    {"Número do Plano": "49", "Nome do Plano": "GEAP CLASS II PA"},
    {"Número do Plano": "50", "Nome do Plano": "GEAP CLASS II PA GRUPO FAMILIAR"},
    {"Número do Plano": "51", "Nome do Plano": "GEAP BASIC I PB"},
    {"Número do Plano": "52", "Nome do Plano": "GEAP BASIC I PB GRUPO FAMILIAR"},
    {"Número do Plano": "53", "Nome do Plano": "GEAP CLASS II PB"},
    {"Número do Plano": "54", "Nome do Plano": "GEAP CLASS II PB GRUPO FAMILIAR"},
    {"Número do Plano": "55", "Nome do Plano": "GEAP BASIC I PE"},
    {"Número do Plano": "56", "Nome do Plano": "GEAP BASIC I PE GRUPO FAMILIAR"},
    {"Número do Plano": "57", "Nome do Plano": "GEAP CLASS II PE"},
    {"Número do Plano": "58", "Nome do Plano": "GEAP CLASS II PE GRUPO FAMILIAR"},
    {"Número do Plano": "59", "Nome do Plano": "GEAP BASIC I RJ"},
    {"Número do Plano": "60","Nome do Plano": "GEAP BASIC I RJ GRUPO FAMILIAR"},
    {"Número do Plano": "61", "Nome do Plano": "GEAP CLASS II RJ"},
    {"Número do Plano": "62", "Nome do Plano": "GEAP CLASS II RJ GRUPO FAMILIAR"},
    {"Número do Plano": "63", "Nome do Plano": "GEAP BASIC I RN"},
    {"Número do Plano": "64", "Nome do Plano": "GEAP BASIC I RN GRUPO FAMILIAR"},
    {"Número do Plano": "65", "Nome do Plano": "GEAP CLASS II RN"},
    {"Número do Plano": "66", "Nome do Plano": "GEAP CLASS II RN GRUPO FAMILIAR"},
    {"Número do Plano": "67", "Nome do Plano": "GEAP BASIC I SP"},
    {"Número do Plano": "68","Nome do Plano": "GEAP BASIC I SP GRUPO FAMILIAR"},
    {"Número do Plano": "69","Nome do Plano": "GEAP CLASS II SP"},
    {"Número do Plano": "70", "Nome do Plano": "GEAP CLASS II SP GRUPO FAMILIAR"},
    {"Número do Plano": "71", "Nome do Plano": "GEAP BASIC II BA"},
    {"Número do Plano": "72", "Nome do Plano": "GEAP BASIC II BA GRUPO FAMILIAR"},
    {"Número do Plano": "73","Nome do Plano": "GEAP CLASS II BA"},
    {"Número do Plano": "74", "Nome do Plano": "GEAP CLASS II BA GRUPO FAMILIAR"},
    {"Número do Plano": "75", "Nome do Plano": "GEAP BASIC II CE"},
    {"Número do Plano": "76", "Nome do Plano": "GEAP BASIC II CE GRUPO FAMILIAR"},
    {"Número do Plano": "77","Nome do Plano": "GEAP CLASS II CE"},
    {"Número do Plano": "78", "Nome do Plano": "GEAP CLASS II CE GRUPO FAMILIAR"},
    {"Número do Plano": "79","Nome do Plano": "GEAP BASIC II PI"},
    {"Número do Plano": "80", "Nome do Plano": "GEAP BASIC II PI GRUPO FAMILIAR"},
    {"Número do Plano": "81", "Nome do Plano": "GEAP CLASS II PI"},
    {"Número do Plano": "82", "Nome do Plano": "GEAP CLASS II PI GRUPO FAMILIAR"},
    {"Número do Plano": "83", "Nome do Plano": "GEAP REFERÊNCIA VIDA II"},
    {"Número do Plano": "84", "Nome do Plano": "GEAP REFERÊNCIA VIDA II GRUPO FAMILIAR"},
    {"Número do Plano": "85","Nome do Plano": "GEAP CLASS II AC"},
    {"Número do Plano": "86", "Nome do Plano": "GEAP CLASS II AC GRUPO FAMILIAR"},
    {"Número do Plano": "87","Nome do Plano": "GEAP CLASS II MA"},
    {"Número do Plano": "88","Nome do Plano": "GEAP CLASS II MA GRUPO FAMILIAR"},
    {"Número do Plano": "89","Nome do Plano": "GEAP CLASS II MS"},
    {"Número do Plano": "90","Nome do Plano": "GEAP CLASS II MS GRUPO FAMILIAR"},
    {"Número do Plano": "91","Nome do Plano": "GEAP CLASS II RS"},
    {"Número do Plano": "92", "Nome do Plano": "GEAP CLASS II RS GRUPO FAMILIAR"},
    {"Número do Plano": "93","Nome do Plano": "GEAP CLASS II SC"},
    {"Número do Plano": "94","Nome do Plano": "GEAP CLASS II SC GRUPO FAMILIAR"},
    {"Número do Plano": "95", "Nome do Plano": "GEAP CLASS II PR"},
    {"Número do Plano": "96", "Nome do Plano": "GEAP CLASS II PR GRUPO FAMILIAR"},
    {"Número do Plano": "97", "Nome do Plano": "GEAP BASIC II AL"},
    {"Número do Plano": "98", "Nome do Plano": "GEAP BASIC II AL GRUPO FAMILIAR"},
    {"Número do Plano": "99", "Nome do Plano": "GEAP BASIC II AM"},
    {"Número do Plano": "100", "Nome do Plano": "GEAP BASIC II AM GRUPO FAMILIAR"},
    {"Número do Plano": "101", "Nome do Plano": "GEAP BASIC II MT"},
    {"Número do Plano": "102", "Nome do Plano": "GEAP BASIC II MT GRUPO FAMILIAR"},
    {"Número do Plano": "103", "Nome do Plano": "GEAP BASIC II RS"},
    {"Número do Plano": "104", "Nome do Plano": "GEAP BASIC II RS GRUPO FAMILIAR"},
    {"Número do Plano": "105", "Nome do Plano": "GEAP BASIC II SE"},
    {"Número do Plano": "106", "Nome do Plano": "GEAP BASIC II SE GRUPO FAMILIAR"},
    {"Número do Plano": "107", "Nome do Plano": "GEAP BASIC II TO"},
    {"Número do Plano": "108", "Nome do Plano": "GEAP BASIC II TO GRUPO FAMILIAR"},
    {"Número do Plano": "109", "Nome do Plano": "GEAP BASIC II PR"},
    {"Número do Plano": "110", "Nome do Plano": "GEAP BASIC II PR GRUPO FAMILIAR"},
    {"Número do Plano": "111", "Nome do Plano": "GEAP BASIC I RR"},
    {"Número do Plano": "112", "Nome do Plano": "GEAP BASIC I RR GRUPO FAMILIAR"},
    {"Número do Plano": "113", "Nome do Plano": "GEAP BASIC I SC"},
    {"Número do Plano": "114", "Nome do Plano": "GEAP BASIC I SC GRUPO FAMILIAR"},
    {"Número do Plano": "115", "Nome do Plano": "GEAP BASIC II ES"},
    {"Número do Plano": "116", "Nome do Plano": "GEAP BASIC II ES GRUPO FAMILIAR"},
    {"Número do Plano": "117", "Nome do Plano": "GEAP BASIC II FG"},
    {"Número do Plano": "118", "Nome do Plano": "GEAP BASIC II FG GRUPO FAMILIAR"},
    {"Número do Plano": "119", "Nome do Plano": "GEAP BASIC II BA"},
    {"Número do Plano": "120", "Nome do Plano": "GEAP BASIC II BA GRUPO FAMILIAR"}
]
     
# Cria uma lista com a sigla  nome do plano para a seleção
planos_opcoes = [f"{p['Nome do Plano']}" for p in planos_dados]
planos_map = {f"{p['Nome do Plano']}": p['Número do Plano'] for p in planos_dados}
#Dados das especialidades
especialidades = [  
    {"Número": "1", "Descrição": "ACUPUNTURA"},
    {"Número": "2", "Descrição": "ALERGIA E IMUNOLOGIA"},
    {"Número": "3", "Descrição": "ANESTESIOLOGIA"},
    {"Número": "4", "Descrição": "ANGIOLOGIA E CIRURGIA VASCULAR"},
    {"Número": "8", "Descrição": "CARDIOLOGIA"},
    {"Número": "10", "Descrição": "CIRURGIA DA CABEÇA E PESCOÇO"},
    {"Número": "11", "Descrição": "CIRURGIA DO APARELHO DIGESTIVO"},
    {"Número": "12", "Descrição": "CIRURGIA GERAL"},
    {"Número": "13", "Descrição": "CIRURGIA PEDIÁTRICA"},
    {"Número": "14", "Descrição": "CIRURGIA PLÁSTICA"},
    {"Número": "15", "Descrição": "CIRURGIA TORÁCICA"},
    {"Número": "16", "Descrição": "CLÍNICA MÉDICA"},
    {"Número": "17", "Descrição": "DERMATOLOGIA"},
    {"Número": "18", "Descrição": "ENDOCRINOLOGIA"},
    {"Número": "19", "Descrição": "ENFERMAGEM"},
    {"Número": "21", "Descrição": "FISIOTERAPIA"},
    {"Número": "22", "Descrição": "ENDOSCOPIA DIGESTIVA"},
    {"Número": "23", "Descrição": "GENÉTICA CLÍNICA"},
    {"Número": "24", "Descrição": "GERIATRIA"},
    {"Número": "25", "Descrição": "GINECOLOGIA E OBSTETRÍCIA"},
    {"Número": "27", "Descrição": "HOMEOPATIA"},
    {"Número": "28", "Descrição": "INFECTOLOGIA"},
    {"Número": "29", "Descrição": "MASTOLOGIA"},
    {"Número": "33", "Descrição": "NUTROLOGIA (MÉDICO)"},
    {"Número": "34", "Descrição": "FISIATRIA (MEDICINA FÍSICA E REABILITAÇÃO)"},
    {"Número": "35", "Descrição": "MEDICINA INTENSIVA"},
    {"Número": "36", "Descrição": "LABORATÓRIO"},
    {"Número": "37", "Descrição": "CIRURGIA DA MÃO"},
    {"Número": "40", "Descrição": "NEFROLOGIA"},
    {"Número": "41", "Descrição": "NEUROCIRURGIA"},
    {"Número": "43", "Descrição": "NUTRIÇÃO"},
    {"Número": "44", "Descrição": "OFTALMOLOGIA"},
    {"Número": "45", "Descrição": "ORTOPEDIA E TRAUMATOLOGIA"},
    {"Número": "46", "Descrição": "OTORRINOLARINGOLOGIA"},
    {"Número": "47", "Descrição": "PEDIATRIA"},
    {"Número": "48", "Descrição": "PNEUMOLOGIA"},
    {"Número": "49", "Descrição": "PROCTOLOGIA"},
    {"Número": "51", "Descrição": "DENSITOMETRIA ÓSSEA"},
    {"Número": "52", "Descrição": "ULTRA-SONOGRAFIA"},
    {"Número": "53", "Descrição": "RADIOTERAPIA"},
    {"Número": "54", "Descrição": "REUMATOLOGIA"},
    {"Número": "55", "Descrição": "UROLOGIA"},
    {"Número": "57", "Descrição": "AUDIOMETRIA"},
    {"Número": "61", "Descrição": "DENTISTA - CLÍNICO GERAL"},
    {"Número": "63", "Descrição": "MAMOGRAFIA"},
    {"Número": "64", "Descrição": "MATERNIDADE"},
    {"Número": "71", "Descrição": "TOMOGRAFIA COMPUTADORIZADA"},
    {"Número": "73", "Descrição": "DENTISTA - PRÓTESES"},
    {"Número": "74", "Descrição": "DENTISTA - ENDODONTIA (TRAT. DE CANAL)"},
    {"Número": "75", "Descrição": "DENTISTA - PERIODONTIA (TRAT. DA GENGIVA)"},
    {"Número": "76", "Descrição": "DENTISTA - ODONTOPEDIATRIA"},
    {"Número": "77", "Descrição": "RADIOLOGIA ODONTOLÓGICA"},
    {"Número": "78", "Descrição": "CIRURGIA BUCO-MAXILO-FACIAL HOSPITALAR"},
    {"Número": "80", "Descrição": "TERAPIA OCUPACIONAL"},
    {"Número": "81", "Descrição": "FONOAUDIOLOGIA"},
    {"Número": "83", "Descrição": "MEDICINA DO TRABALHO"},
    {"Número": "84", "Descrição": "CARDIOLOGIA PEDIÁTRICA"},
    {"Número": "85", "Descrição": "GASTROENTEROLOGIA PEDIÁTRICA"},
    {"Número": "86", "Descrição": "NEFROLOGIA PEDIÁTRICA"},
    {"Número": "87", "Descrição": "NEUROLOGIA PEDIÁTRICA"},
    {"Número": "88", "Descrição": "PNEUMOLOGIA PEDIÁTRICA"},
    {"Número": "90", "Descrição": "NEUROLOGIA"},
    {"Número": "91", "Descrição": "RADIOLOGIA MÉDICA"},
    {"Número": "92", "Descrição": "RESSONÂNCIA MAGNÉTICA"},
    {"Número": "93", "Descrição": "GASTROENTEROLOGIA"},
    {"Número": "97", "Descrição": "QUIMIOTERAPIA"},
    {"Número": "100", "Descrição": "COLONOSCOPIA"},
    {"Número": "102", "Descrição": "ENDOSCOPIA RESPIRATÓRIA"},
    {"Número": "103", "Descrição": "TRATAMENTO DA DOR"},
    {"Número": "104", "Descrição": "POLISSONOGRAFIA"},
    {"Número": "107", "Descrição": "ELETRONEUROMIOGRAFIA"},
    {"Número": "108", "Descrição": "ELETROENCEFALOGRAMA"},
    {"Número": "109", "Descrição": "CINTILOGRAFIA"},
    {"Número": "110", "Descrição": "HEPATOLOGIA"},
    {"Número": "111", "Descrição": "CITOPATOLOGIA"},
    {"Número": "113", "Descrição": "NEONATOLOGIA"},
    {"Número": "116", "Descrição": "TESTE ERGOMÉTRICO"},
    {"Número": "117", "Descrição": "ELETROCARDIOGRAMA"},
    {"Número": "119", "Descrição": "HOLTER"},
    {"Número": "120", "Descrição": "MAPA"},
    {"Número": "123", "Descrição": "DOPPLER COLORIDO"},
    {"Número": "124", "Descrição": "COLPOSCOPIA"},
    {"Número": "126", "Descrição": "HEMODIÁLISE"},
    {"Número": "129", "Descrição": "PET SCAN"},
    {"Número": "132", "Descrição": "HEMATOLOGIA"},
    {"Número": "133", "Descrição": "HEMOTERAPIA"},
    {"Número": "136", "Descrição": "OXIGENOTERAPIA"},
    {"Número": "137", "Descrição": "ANATOMIA PATOLÓGICA"},
    {"Número": "138", "Descrição": "ENDOCRINOLOGIA PEDIÁTRICA"},
    {"Número": "146", "Descrição": "TOMOGRAFIA COMPUTADORIZADA ODONTOLOGICA"},
    {"Número": "147", "Descrição": "ECOCARDIOGRAFIA"},
    {"Número": "148", "Descrição": "MEDICINA NUCLEAR"},
    {"Número": "149", "Descrição": "ATENDIMENTO AO QUEIMADO"},
    {"Número": "150", "Descrição": "PSIQUIATRIA"},
    {"Número": "151", "Descrição": "HEMODINÂMICA / CARDIOLOGIA INTERVENCIONISTA"},
    {"Número": "152", "Descrição": "CIRURGIA CARDIOVASCULAR"},
    {"Número": "153", "Descrição": "CANCEROLOGIA"},
    {"Número": "154", "Descrição": "PSICOLOGIA"},
    {"Número": "156", "Descrição": "DENTISTA - ODONTOPEDIATRIA / PREVENÇÃO"},
    {"Número": "157", "Descrição": "DENTISTA BUCO-MAXILO-FACIAL AMBULATORIAL"},
    {"Número": "158", "Descrição": "MEDICINA ESPORTIVA"},
    {"Número": "159", "Descrição": "MEDICINA DA FAMÍLIA E COMUNIDADE"},
    {"Número": "160", "Descrição": "CIRURGIA ONCOLÓGICA"},
    {"Número": "161", "Descrição": "MEDICINA DE EMERGÊNCIA"},
    {"Número": "162", "Descrição": "MEDICINA LEGAL E PERÍCIA MÉDICA"},
    {"Número": "163", "Descrição": "ONCOLOGIA CLÍNICA"},
    {"Número": "164", "Descrição": "PATOLOGIA"},
    {"Número": "165", "Descrição": "PATOLOGIA CLÍNICA / MEDICINA LABORATORIAL"},
    {"Número": "166", "Descrição": "RADIOLOGIA E DIAGNÓSTICO POR IMAGEM"},
    {"Número": "167", "Descrição": "RADIOTERAPIA"},
    {"Número": "168", "Descrição": "MEDICINA DO TRÁFEGO"},
    {"Número": "169", "Descrição": "CIRURGIA VASCULAR"},
    {"Número": "170", "Descrição": "ANGIOLOGIA"},
    {"Número": "171", "Descrição": "MÉDICO GENERALISTA"},
]


# Cria uma lista com a descrição para a seleção
especialidades_opcoes = [e['Descrição'] for e in especialidades]
especialidades_map = {e['Descrição']: e['Número'] for e in especialidades}

# Título da aplicação
st.title('Área do Parametrizador')

# Seção de Dados do Prestador
st.subheader('Dados do Prestador')
col1, col2 = st.columns(2)

with col1:
    cod_prestador = st.text_input('Código do Prestador')
    catalogo_id = st.text_input('Catálogo ID')

with col2:
    dta_ini_validade = st.date_input('Data Início Validade')
    dta_fim_validade = st.date_input('Data Fim Validade')

# Seção de Parâmetros da Especialidade
st.subheader('Parâmetros da Especialidade')

especialidade_selecionada = st.multiselect('Escolha uma ou mais Especialidades', options=especialidades_opcoes)

col1, col2, col3 = st.columns(3)

with col1:
    sta_atendimento_pediatrico = st.selectbox('Atendimento Pediátrico', options=['1 - Sim', '0 - Não'])
    sta_proprio = st.selectbox('Proprio', options=['1 - Sim', '0 - Não'])
    sta_hora_marcada = st.selectbox('Hora Marcada', options=['1 - Sim', '0 - Não'])

with col2:
    sta_encaminha_util_movel = st.selectbox('Encaminha Util Móvel', options=['1 - Sim', '0 - Não'])
    sta_paciente_internado = st.selectbox('Paciente Internado', options=['1 - Sim', '0 - Não'])
    sta_programa_viva_melhor = st.selectbox('Programa Viva Melhor', options=['1 - Sim', '0 - Não'])

with col3:
    sta_tele_ssaude = st.selectbox('Tele Saúde', options=['1 - Sim', '0 - Não'])
    sta_urgente_emergencia = st.selectbox('Urgente Emergência', options=['1 - Sim', '0 - Não'])
    sta_pronto_atendimento = st.selectbox('Pronto Atendimento', options=['1 - Sim', '0 - Não'])

# Seleção de múltiplos planos
st.subheader('Seleção de Planos')
planos_selecionados = st.multiselect('Escolha um ou mais Planos', options=planos_opcoes)

# Botão para cadastrar especialidade
if st.button('Cadastrar Especialidade'):
    dados = []
    for plano_selecionado in planos_selecionados:
        plano_numero = planos_map[plano_selecionado]
        for especialidade in especialidade_selecionada:
            dados.append({
                'CodPrestador': cod_prestador,
                'CatalogoId': catalogo_id,
                'DtaIniValidade': formatar_data(dta_ini_validade),
                'DtaFimValidade': formatar_data(dta_fim_validade),
                'NroPlano': plano_numero,
                'Especialidade': especialidades_map[especialidade],  # Armazena o número da especialidade
                'StaAtendimentoPediatrico': sta_atendimento_pediatrico.split(' - ')[0],
                'StaProprio': sta_proprio.split(' - ')[0],
                'StaHoraMarcada': sta_hora_marcada.split(' - ')[0],
                'StaEncaminhaUtilMovel': sta_encaminha_util_movel.split(' - ')[0],
                'StaPacienteInternado': sta_paciente_internado.split(' - ')[0],
                'StaProgramaVivaMelhor': sta_programa_viva_melhor.split(' - ')[0],
                'StaUrgenteEmergencia': sta_urgente_emergencia.split(' - ')[0],
                'StaProntoAtendimento': sta_pronto_atendimento.split(' - ')[0],
                'StaTeleSsaude': sta_tele_ssaude.split(' - ')[0],
            })
    
    st.session_state.dados.extend(dados)
    st.success('Especialidades cadastradas com sucesso!')

# Exibe a tabela com os dados cadastrados
if st.session_state.dados:
    st.subheader('Tabela de Especialidades Cadastradas')
    df = pd.DataFrame(st.session_state.dados)
    
    # Formata as datas para o padrão brasileiro
    df['DtaIniValidade'] = df['DtaIniValidade'].apply(lambda x: formatar_data(pd.to_datetime(x)))
    df['DtaFimValidade'] = df['DtaFimValidade'].apply(lambda x: formatar_data(pd.to_datetime(x)))

    st.dataframe(df)

    # Função para converter DataFrame para CSV
    def to_csv(df):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False, sep=',', date_format='%d/%m/%Y')  # Usa vírgula como delimitador e formata data
        return csv_buffer.getvalue()

    # Botão para salvar a tabela em CSV
    csv = to_csv(df)
    st.download_button(
        label="Salvar como CSV",
        data=csv,
        file_name='especialidades_cadastradas.csv',
        mime='text/csv'
    )

# Botões para limpar tabela e formulário
col1, col2 = st.columns(2)

with col1:
    if st.button('Limpar Tabela'):
        st.session_state.dados = []  # Limpa os dados do estado
        st.success('Tabela limpa com sucesso!')
        st.experimental_rerun()  # Atualiza a página para refletir as mudanças

with col2:
    if st.button('Limpar Formulário'):
        st.experimental_rerun()  # Limpa todos os campos do formulário e reinicia a aplicação
