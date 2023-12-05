# Importer les classes nécessaires du module forex_python.converter
from forex_python.converter import CurrencyRates, RatesNotAvailableError
# Importer le module datetime pour manipuler les dates et les heures
import datetime

# Créer une instance de CurrencyRates
cr = CurrencyRates()

try:
    # Demander à l'utilisateur d'entrer le montant à convertir
    amount = int(input("Veuillez entrer le montant que vous souhaitez convertir: "))

    # Demander à l'utilisateur d'entrer le code de la devise à convertir
    from_currency = input("Veuillez entrer le code de la devise à convertir: ").upper()

    # Demander à l'utilisateur d'entrer le code de la devise dans laquelle convertir
    to_currency = input("Veuillez entrer le code de la devise dans laquelle convertir: ").upper()
    
    # Afficher les détails de la conversion
    print("Vous convertissez", amount, from_currency, "en", to_currency,".")

    # Effectuer la conversion
    output = cr.convert(from_currency, to_currency, amount)

    # Afficher le taux converti
    print("Le taux converti est:", output)

    # Sauvegarder les détails de la conversion dans un fichier
    with open('historique_des_conversions.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()}: Converti {amount} {from_currency} en {to_currency}. Le taux converti est : {output}\n")

except RatesNotAvailableError:
     # Si la conversion n'est pas possible, afficher un message d'erreur
    print("Désolé, la conversion entre", from_currency, "et", to_currency, "n'est pas possible. Veuillez vérifier les codes de devises.")
    
# Ajouter une devise et son taux de conversion
devise = input("Veuillez entrer le code de la devise que vous souhaitez ajouter: ").upper()
taux = float(input("Veuillez entrer le taux de conversion pour cette devise: "))

# Ajouter la devise et son taux de conversion à la liste des devises préférées de l'utilisateur
devises_preferees = {}
devises_preferees[devise] = taux

# Afficher les devises préférées de l'utilisateur
print("Vos devises préférées sont:", devises_preferees)