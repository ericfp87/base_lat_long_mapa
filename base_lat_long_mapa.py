import pandas as pd
import unicodedata
import pyarrow


def remove_accents(input_str):
    if isinstance(input_str, str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
    else:
        return input_str

matriculas = r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\cep_matr_loc_logr.csv"
coord = r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\LOGRADOUROS_MG_UPPER.csv"
mun_lat_long = r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\MUNICIPIOS_LAT_LONG_UPPER.csv"



print("Lendo Arquivos")
df_matr = pd.read_csv(matriculas, delimiter=';')
df_coord = pd.read_csv(coord, delimiter=';')
df_mun_lat_long = pd.read_csv(mun_lat_long, delimiter=";")

#Removendo espaços
df_matr = df_matr.apply(lambda x: x.strip() if isinstance(x, str) else x)
df_coord = df_coord.apply(lambda x: x.strip() if isinstance(x, str) else x)
df_mun_lat_long = df_mun_lat_long.apply(lambda x: x.strip() if isinstance(x, str) else x)

#Letras Maiusculas sem acento
df_mun_lat_long['Municipio'] = df_mun_lat_long['Municipio'].str.upper().apply(remove_accents)
df_mun_lat_long['Logradouro'] = df_mun_lat_long['Logradouro'].str.upper().apply(remove_accents)


print("Junção entre matr_loc_logr.csv e LOGRADOUROS_MG_UPPER.csv")
df_joined = pd.merge(df_coord, df_matr, left_on=["cep"], right_on=["CEP"], how='right')



df_final = df_joined[['Matricula','Nome_Localidade','district','Nome_logradouro','CEP','lat','lng']]
#df_final.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\01df_final.csv",sep=';',index=False, mode='w')

#Dataframe Completo
df_city_not_empty = df_final[df_final['lat'].notna()]
#df_city_not_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\02df_city_not_empty.csv",sep=';',index=False, mode='w')

#Dataframe sem dados
df_city_empty = df_final[df_final['lat'].isna()]
#df_city_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\03df_city_empty.csv",sep=';',index=False, mode='w')

print("Junção entre vazios de matr_loc_logr.csv e LOGRADOUROS_MG_UPPER.csv")
df_city_empty_merge01 = pd.merge(df_city_empty, df_coord, how='left', left_on=['Nome_Localidade', 'Nome_logradouro'], right_on=['city', 'address_name'])


df_city_01 = df_city_empty_merge01[['Matricula','Nome_Localidade','district_x','Nome_logradouro','CEP','lat_y','lng_y']]
df_city_01 = df_city_01.rename(columns={'lat_y': 'lat', 'lng_y': 'lng', 'district_x': 'district'})
#df_city_01.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\04df_city_01.csv",sep=';',index=False, mode='w')

#Dataframe Completo
df_city_not_empty02 = df_city_01[df_city_01['lat'].notna()]
#df_city_not_empty02.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\04df_city_not_empty02.csv",sep=';',index=False, mode='w')

#Dataframe sem dados
df_city_empty = df_city_01[df_city_01['lat'].isna()]
#df_city_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\04df_city_empty02.csv",sep=';',index=False, mode='w')

print("Unindo dataframe completo")
df_city_not_empty = pd.concat([df_city_not_empty, df_city_not_empty02])
print("OK")




#df_city_empty = df_city_empty[['CEP']]
#df_city_empty = df_city_empty.drop_duplicates(subset='CEP')
print("Junção entre vazios de matr_loc_logr.csv e MUNICIPIOS_LAT_LONG_UPPER.csv")
df_city_empty_merge = pd.merge(df_city_empty, df_mun_lat_long, how='left', left_on=['Nome_Localidade', 'Nome_logradouro'], right_on=['Municipio', 'Logradouro'])
#df_city_empty_merge.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\05df_city_empty_merge.csv",sep=';',index=False, mode='w')


df_city_empty_merge = df_city_empty_merge[['Matricula','Nome_Localidade','district','Nome_logradouro','CEP','LAT','LONG']]
df_city_empty_merge = df_city_empty_merge.rename(columns={'LAT': 'lat', 'LONG': 'lng'})

#df_city_empty_merge.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\06df_city_empty_merge.csv",sep=';',index=False, mode='w')

df_merge_not_empty = df_city_empty_merge[df_city_empty_merge['lat'].notna()]
#df_merge_not_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\07df_merge_not_empty.csv",sep=';',index=False, mode='w')

df_city_empty = df_city_empty_merge[df_city_empty_merge['lat'].isna()]
#df_city_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\08df_city_empty.csv",sep=';',index=False, mode='w')

# Concatenar os dataframes
print("Concatenando")
df_concatenated_not_empty = pd.concat([df_city_not_empty, df_merge_not_empty])

df_total = pd.concat([df_concatenated_not_empty, df_city_empty])

df_cep_lat_long = df_total[['Nome_Localidade','district','Nome_logradouro','CEP','lat','lng']]
df_cep_lat_long = df_cep_lat_long.drop_duplicates()



print("Gerando CSV")
df_concatenated_not_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\base_cep_matr.csv",sep=';',index=False, mode='w')
df_city_empty.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\CEP_Inexistente.csv",sep=';',index=False, mode='w')
df_total.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\BASE_MATR_LOG_TOTAL.csv",sep=';',index=False, mode='w')
df_cep_lat_long.to_csv(r"C:\Files\BASE LATITUDE LONGITUDE\CEP\TESTE\TESTE 3 BASES\OUTPUT\BASE_CEP_LAT_LONG.csv",sep=';',index=False, mode='w')

print("Gerando parquet")
df_total.to_parquet(r"C:\Files\BASE LATITUDE LONGITUDE\BASE_MATR_LOG_TOTAL.parquet", engine='pyarrow')
df_cep_lat_long.to_parquet(r"C:\Files\BASE LATITUDE LONGITUDE\BASE_CEP_LAT_LONG.parquet", engine='pyarrow')

print("Concluído")
