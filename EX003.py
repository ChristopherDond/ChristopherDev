# EX 3 arrumado
 
def br_currency(value: float) -> str:
    """Formata numero: 1.234,56"""
    s = f"{value:,.2f}"              
    s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
    return f"R$ {s}"
 
def input_float(prompt: str, default: float | None = None, allow_zero=True) -> float:
    """Lê float do usuario; se vazio e default fornecido, usa default valida nao negativo"""
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            val = float(raw.replace(',', '.'))
            if val < 0 or (not allow_zero and val == 0):
                print("  Valor inválido: insira um número não negativo.")
                continue
            return val
        except ValueError:
            print("  Entrada inválida, digite um número (use '.' ou ',' para decimais).")
 
def input_int(prompt: str, default: int | None = None) -> int:
    """Lê inteiro do usuário; se vazio e default fornecido, usa default, valida nao negativo."""
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            val = int(raw)
            if val < 0:
                print("  Valor inválido: insira um inteiro não negativo.")
                continue
            return val
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro não-negativo.")
 
def calcula_inss_progressivo(base: float) -> (float, float):
    """
    Calcula INSS progressivo pelas faixas informadas:
    até 1.412,00 -> 7,5%
    1.412,01–2.666,68 -> 9%
    2.666,69–4.000,03 -> 12%
    4.000,04–7.786,02 -> 14%
    Com teto de contribuição: R$ 908,85
    Retorna (valor_inss, aliquota_efetiva_em_porcento)
    """
    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14),
    ]
    restante = base
    contribuicao = 0.0
    inferior = 0.0
    for limite, taxa in faixas:
        if restante <= 0:
            break
        faixa_valor = max(0.0, min(limite - inferior, restante))
        contribuicao += faixa_valor * taxa
        restante -= faixa_valor
        inferior = limite

    teto = 908.85
    if contribuicao > teto:
        contribuicao = teto
    aliquota_efetiva = (contribuicao / base * 100) if base > 0 else 0.0
    return round(contribuicao, 2), round(aliquota_efetiva, 2)
 
def calcula_irrf(taxa_base: float, dependentes: int, deducao_por_dependente: float = 0.0):
    """
    Calcula IRRF com as faixas informadas:
    Base do IRRF: taxa_base (salário bruto + bonus) - INSS - (dependentes * deducao_por_dependente)
    Faixas:
      até 2.259,20 -> isento
      2.259,21–3.823,98 -> 7,5% (dedução R$ 169,44)
      3.823,99–5.105,94 -> 15% (dedução R$ 381,44)
      acima -> 22,5% (dedução R$ 662,77)
    Retorna (valor_irrf, aliquota_aplicada_percent, aliquota_efetiva_percent, base_tributavel)
    """
    
    faixas = [
        (2259.20, 0.0, 0.0),
        (3823.98, 0.075, 169.44),
        (5105.94, 0.15, 381.44),
        (float('inf'), 0.225, 662.77),
    ]
    base_tributavel = taxa_base - dependentes * deducao_por_dependente
    if base_tributavel < 0:
        base_tributavel = 0.0
 
    aliquota = 0.0
    deducao = 0.0
    for limite, a, d in faixas:
        if base_tributavel <= limite:
            aliquota = a
            deducao = d
            break
 
    if aliquota == 0.0:
        irrf = 0.0
    else:

        irrf = base_tributavel * aliquota - deducao
        if irrf < 0:
            irrf = 0.0
 
    aliquota_efetiva = (irrf / base_tributavel * 100) if base_tributavel > 0 else 0.0
    return round(irrf, 2), round(aliquota * 100, 2), round(aliquota_efetiva, 2), round(base_tributavel, 2)
 
def main():
    print("=== Calculadora de Salário Líquido (Regras fornecidas) ===\n")
    salario_bruto = input_float("Salário bruto mensal (ex: 3500,50): R$ ", None)
    bonus = input_float("Bônus (opcional, Enter = 0): R$ ", default=0.0)
    dependentes = input_int("Número de dependentes (Enter = 0): ", default=0)

    ded_dep = input("Valor de dedução por dependente (Enter = 0, use '.' ou ',' para decimais): ").strip()
    if ded_dep == "":
        ded_dep_val = 0.0
    else:
        try:
            ded_dep_val = float(ded_dep.replace(',', '.'))
            if ded_dep_val < 0:
                print("Valor de dedução inválido; usando 0.")
                ded_dep_val = 0.0
        except ValueError:
            print("Entrada inválida; usando 0.")
            ded_dep_val = 0.0
 
   
    vt_option = input("Deseja descontar Vale Transporte (6% sobre salário bruto)? (s/n) [n]: ").strip().lower()
    desconto_vt = 0.0
    if vt_option == "s" or vt_option == "sim":
        desconto_vt = round(0.06 * salario_bruto, 2)
 

    vr_input = input("Deseja Vale Refeição? Enter para usar R$500, digite 0 para não, ou informe outro valor: ").strip()
    if vr_input == "":
        desconto_vr = 500.00
    else:
        try:
            vr_val = float(vr_input.replace(',', '.'))
            if vr_val < 0:
                print("Valor inválido para VR; usando R$0,00.")
                desconto_vr = 0.0
            else:
                desconto_vr = vr_val
        except ValueError:
            print("Entrada inválida para VR; usando R$0,00.")
            desconto_vr = 0.0
 
    base_total = salario_bruto + bonus
 
    valor_inss, aliquota_inss_efet = calcula_inss_progressivo(base_total)
 
    base_irrf = base_total - valor_inss
    valor_irrf, aliquota_irrf_aplicada, aliquota_irrf_efet, base_tributavel = calcula_irrf(base_irrf, dependentes, ded_dep_val)
 
    total_descontos = round(valor_inss + valor_irrf + desconto_vt + desconto_vr, 2)
    salario_liquido = round(base_total - total_descontos, 2)
 
    print("\n=== Resumo ===")
    print(f"Salário bruto:            {br_currency(salario_bruto)}")
    print(f"Bônus:                    {br_currency(bonus)}")
    print(f"Base total (salário+bônus): {br_currency(base_total)}\n")
 
    print("--- Descontos ---")
    print(f"INSS:                     {br_currency(valor_inss)} (alíquota efetiva: {aliquota_inss_efet:.2f}%)")
    print(f"IRRF:                     {br_currency(valor_irrf)} (alíquota tabela aplicada: {aliquota_irrf_aplicada:.2f}%; alíquota efetiva sobre base tributável: {aliquota_irrf_efet:.2f}%)")
    print(f"  Base tributável IRRF:   {br_currency(base_tributavel)}")
    print(f"Vale Transporte (6% opt.):{br_currency(desconto_vt)}")
    print(f"Vale Refeição:            {br_currency(desconto_vr)}")
 
    print("\n--- Totais ---")
    print(f"Total de descontos:       {br_currency(total_descontos)}")
    print(f"Salário líquido final:    {br_currency(salario_liquido)}")

    aliquota_inss_rel_bruto = (valor_inss / base_total * 100) if base_total > 0 else 0.0
    aliquota_irrf_rel_bruto = (valor_irrf / base_total * 100) if base_total > 0 else 0.0
    print("\n--- Alíquotas (referência) ---")
    print(f"INSS efetivo sobre bruto: {aliquota_inss_rel_bruto:.2f}%")
    print(f"IRRF efetivo sobre bruto: {aliquota_irrf_rel_bruto:.2f}%")
    print("\n(Observação: dependentes e deduções podem alterar a base do IRRF.)")
    print("\nFim.")
 
 
if __name__ == "__main__":
    main()