df_futbol.info()
different_values = df_futbol['Manager'].unique()
print("Different values in column 'Manager':", different_values)
#differents values in column 'Team'

different_values = df_futbol['Team'].unique()
print("Different values in column 'Team':", different_values)

#get promedio of Shots_on_target from df_futbol
promedio_shots_on_target = df_futbol['Shots_on_target'].mean()
print("Average Shots_on_target:", promedio_shots_on_target)

#complete the nulls values from Shots_on_target with de average
# Complete the null values in the 'Shots_on_target' column with the average
df_futbol['Shots_on_target'].fillna(df_futbol['Shots_on_target'].mean(), inplace=True)

#get the values of column Field_zone
field_zone_values = df_futbol['Field_zone'].values
print("Values of column 'Field_zone':", field_zone_values)


#Complete the null values in the 'Manager' with the string 'Other'
# Complete the null values in the 'Manager' column with the string 'Other'
df_futbol['Manager'].fillna('Other', inplace=True)
#delete the column 'Passes'
df_futbol.drop('Passes', axis=1, inplace=True)

#replace in column