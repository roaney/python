itens = ["cadeira", "mesa", "lâmpada", "sofá", "estante"]

item_procurado = "tv"
encontrado = False

print("--- Usando BREAK para parar a busca ---")
for item in itens:
    print(f"Analisando: {item}")
    
    if item == item_procurado:
        print(f"🎉 Encontrado! O item é: {item}")
        encontrado = True
        break  # Sai imediatamente do loop 'for'
        
if not encontrado:
    print("Item não encontrado.")
    
# Saída (Note que "sofá" e "estante" não são analisados):
# --- Usando BREAK para parar a busca ---
# Analisando: cadeira
# Analisando: mesa
# Analisando: lâmpada
# 🎉 Encontrado! O item é: lâmpada