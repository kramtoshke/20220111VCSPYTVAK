
text = 'hello world'

print (text)


num = 156
print(num + 5 - 1056)
print(text)

# # Kintamuju pavadinimai

# 1st_name = 'Darius' # negali prasideti skaiciumi
name_1 = 'Darius'

# %%
print(sum([1 , 2, 5, 8]) )
# sum = 0 # nebeveiks sum() funkcija. Visos standartines funkcijos: https://docs.python.org/3/library/functions.html
# reikia 
print(sum([1 , 2, 5, 8]) )

# %% [markdown]
# # String

# %%
print (text)

# %%
print (text[4] ) # indexing
print (text[0] )
print (text[6] )
print (text[10] )
print (text[-1] ) # tas pats kas text[10]
print (text[-2] )

# %%
text_2 = "hello beautiful world"
print (text_2[10] )
print (text_2[-1] )

# %% [markdown]
# ### Slicing

# %%
print       (  text_2      [0:5]     )
print (text_2[:5] ) # 0 nera butinas
print                (text_2[6:15] )
print (text_2[6:-1] ) # neitraukia 'd' raides
print (text_2[6:] )
print (text_2[6:15:2] ) 
# slicing [start:end:step]
# apsukti teksta
print (text_2[::-1] )

# %% [markdown]
# ## operations

# %%
text + ' ' + text_2

# %%
# text_2 - text # negalima

# %%


'hi ' * 10

# %%
# 'hi ' / 'i' # negalima

# %%
text_3 = 'Some text'

# %%
print(text_3)

# %%
print(len(''))
print(len('hello'))
print(len('  hello   '))


