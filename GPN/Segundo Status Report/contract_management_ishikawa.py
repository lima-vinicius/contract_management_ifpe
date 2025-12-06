import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import textwrap

# Configuração de estilo de fonte
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']

def criar_ishikawa_final(problema, causas_dict, nome_arquivo):
    """
    Gera um diagrama de Ishikawa com layout corrigido.
    Foco: Cabeça do peixe visível com texto do problema e layout de espinhas organizado.
    """
    
    # 1. Configuração da Área de Desenho (Canvas)
    # Aumentei o width para 26 para caber a cabeça confortavelmente
    fig, ax = plt.subplots(figsize=(26, 14), facecolor='white')
    ax.set_xlim(0, 26) 
    ax.set_ylim(-10, 10)
    ax.axis('off')
    
    # Paleta de Cores
    cores = {
        'MÉTODO': '#E63946',       # Vermelho
        'MÃO DE OBRA': '#F4A261',  # Laranja
        'MATERIAL': '#E9C46A',     # Amarelo
        'MÁQUINA': '#2A9D8F',      # Verde
        'MEDIDA': '#264653',       # Azul Escuro
        'MEIO AMBIENTE': '#8E44AD' # Roxo
    }
    
    cats_top = ['MÁQUINA', 'MÉTODO', 'MEDIDA']
    cats_bottom = ['MÃO DE OBRA', 'MATERIAL', 'MEIO AMBIENTE']
    
    # ==========================================
    # 2. DESENHAR A ESPINHA E A CABEÇA (CORRIGIDO)
    # ==========================================
    spine_start = 1
    spine_end = 20
    
    # Linha central (Espinha)
    ax.plot([spine_start, spine_end], [0, 0], color='#333333', lw=6, zorder=1)
    
    # --- DESENHO DA CABEÇA DO PEIXE ---
    # Coordenadas
    head_start_x = spine_end
    head_width = 5.5
    head_height = 4
    
    # 1. Triângulo de conexão (Pescoço)
    triangle = patches.Polygon(
        [[head_start_x, 0], [head_start_x + 1, 1], [head_start_x + 1, -1]], 
        closed=True, color='#2B2D42', zorder=2
    )
    ax.add_patch(triangle)
    
    # 2. Retângulo Arredondado (A Cabeça/Caixa do Texto)
    box_x = head_start_x + 0.8
    box_y = - (head_height / 2) # Centralizar verticalmente
    
    head_box = patches.FancyBboxPatch(
        (box_x, box_y), head_width, head_height,
        boxstyle="round,pad=0.2,rounding_size=0.4",
        linewidth=0, color='#2B2D42', zorder=2
    )
    ax.add_patch(head_box)
    
    # 3. Texto do Problema (CORRIGIDO)
    # Quebra o texto em linhas curtas para caber na caixa
    wrap_prob = textwrap.fill(problema, width=22)
    
    ax.text(
        box_x + (head_width / 2), 0, # X e Y (Centro da caixa)
        wrap_prob, 
        ha='center', va='center', 
        fontsize=13, fontweight='bold', color='white', 
        linespacing=1.5, zorder=10
    )

    # ==========================================
    # 3. DESENHO DAS COSTELAS E CAUSAS
    # ==========================================
    def desenhar_ramo(categoria, x_pos, is_top):
        cor = cores.get(categoria, '#999999')
        causas = causas_dict.get(categoria, [])
        
        altura_costela = 7.5
        direcao = 1 if is_top else -1
        angulo_x_offset = 2.5
        
        # Linha da Categoria (Diagonal)
        start_point = (x_pos, 0)
        end_point = (x_pos + angulo_x_offset, altura_costela * direcao)
        
        ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 
                color=cor, lw=3, alpha=0.85, zorder=2)
        
        # Etiqueta da Categoria
        bbox_props = dict(boxstyle="round,pad=0.4", fc=cor, ec="none", alpha=1)
        ax.text(end_point[0], end_point[1] + (0.6 * direcao), categoria, 
                ha='center', va='center', fontsize=11, fontweight='bold', 
                color='white', bbox=bbox_props, zorder=5)
        
        # Desenhar Causas
        num_causas = len(causas)
        if num_causas == 0: return

        # Ajuste de espaçamento para evitar sobreposição na espinha
        margem_espinha = 1.0 
        step_y = (altura_costela - margem_espinha) / num_causas
        
        for i, causa in enumerate(causas):
            pos_relativa = (i + 1)
            # Calcula Y considerando a margem da espinha
            y_curr = (margem_espinha + (step_y * i)) * direcao
            
            # Calcula X na diagonal
            pct_altura = abs(y_curr) / altura_costela
            x_curr = x_pos + (angulo_x_offset * pct_altura)
            
            # Linha horizontal da causa
            comp_galho = 0.6
            ax.plot([x_curr, x_curr + comp_galho], [y_curr, y_curr], 
                    color=cor, lw=1.5, ls='-', zorder=3)
            
            # Texto da Causa
            texto_wrap = textwrap.fill(causa, width=28)
            
            txt = ax.text(x_curr + comp_galho + 0.15, y_curr, texto_wrap, 
                          fontsize=9, va='center', ha='left', 
                          color='#333333', fontweight='medium', zorder=4)
            # Contorno branco para legibilidade
            txt.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])

    # Posições fixas (Zig-Zag)
    posicoes_x_top = [3, 9, 15]
    posicoes_x_bot = [6, 12, 17.5] # Afastei um pouco mais o último de baixo
    
    for i, cat in enumerate(cats_top):
        if i < len(posicoes_x_top): desenhar_ramo(cat, posicoes_x_top[i], True)
            
    for i, cat in enumerate(cats_bottom):
        if i < len(posicoes_x_bot): desenhar_ramo(cat, posicoes_x_bot[i], False)

    # Rodapé
    ax.text(1, -9.5, 'IFPE - Projeto Gestão de Contratos | Diagrama de Causa e Efeito (Ishikawa)', 
            fontsize=10, color='#777777', style='italic')

    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Diagrama gerado com sucesso: {nome_arquivo}")

# =================================================================
# DADOS
# =================================================================

causas_descentralizacao = {
    'MÉTODO': ['Falta de governança de dados', 'Fluxo não centralizado', 'Sem padrão de registro', 'Comunicação em silos'],
    'MÃO DE OBRA': ['Sem "dono" dos dados', 'Gestores isolados nos campi', 'Falta de backup/cross-training', 'Sem responsável pela integridade'],
    'MATERIAL': ['Docs em repositórios diversos', 'Planilhas locais (Excel) isoladas', 'Uso de e-mail como arquivo', 'Pastas físicas individuais'],
    'MÁQUINA': ['Inexistência de ERP/Sistema único', 'Sem integração de sistemas', 'Ferramentas díspares (Sheets vs Excel)', 'Sem banco de dados central'],
    'MEDIDA': ['Sem indicadores de centralização', 'Sem auditoria de integridade', 'Não se mede tempo de busca', 'Métricas inexistentes'],
    'MEIO AMBIENTE': ['Cultura de descentralização', 'Autonomia excessiva dos campi', 'Resistência à mudança', 'Estrutura fragmentada']
}

causas_atrasos = {
    'MÉTODO': ['Processo manual/informal', 'Sem POP de renovação', 'Trilhas A/B indefinidas', 'Repactuação complexa'],
    'MÃO DE OBRA': ['Sobrecarga de trabalho', 'Rotatividade de gestores', 'Acúmulo de funções', 'Equipes sem apoio'],
    'MATERIAL': ['Calendários não compartilhados', 'Índices (IPCA) desatualizados', 'Docs difíceis de localizar', 'Histórico disperso'],
    'MÁQUINA': ['Sem alertas (6 e 3 meses)', 'Sem notificações push/email', 'Sem cálculo de prazos', 'Sistemas não integrados'],
    'MEDIDA': ['Sem controle de SLA', 'Não se mede taxa de renovação', 'Sem monitoramento de risco', 'Prazos invisíveis'],
    'MEIO AMBIENTE': ['Cultura reativa ("apagar incêndio")', 'Burocracia externa (CGU)', 'Baixa prioridade estratégica', 'Fluxos de aprovação lentos']
}

causas_padronizacao = {
    'MÉTODO': ['Organização "ad-hoc"', 'Sem templates padrão', 'Sem checklist de fiscalização', 'Onboarding inexistente'],
    'MÃO DE OBRA': ['Fiscais desconhecem papéis', 'Falta treinamento Lei 14.133', 'Desnível de experiência', 'Comunicação falha'],
    'MATERIAL': ['Docs sem metadados', 'Versionamento confuso', 'Arquivos perdidos em drives', 'Sem repositório oficial'],
    'MÁQUINA': ['Sem DMS (Gestão Documental)', 'Sem campos obrigatórios', 'Permissões de acesso falhas', 'Tecnologia não padronizada'],
    'MEDIDA': ['Sem auditoria de padrão', 'Sem critérios de qualidade', 'Não há benchmark entre campi', 'Conformidade não medida'],
    'MEIO AMBIENTE': ['Resistência cultural', 'Maturidade digital desigual', 'Falta de liderança central', 'Política institucional fraca']
}

# =================================================================
# EXECUÇÃO
# =================================================================

if __name__ == "__main__":
    print("Gerando diagramas finais corrigidos...")
    
    criar_ishikawa_final(
        "Descentralização das Informações: Dados dispersos e sem visão única", 
        causas_descentralizacao, 
        "Ishikawa_1_Final.png"
    )
    
    criar_ishikawa_final(
        "Atrasos na Renovação: Risco de interrupção e perda de prazos", 
        causas_atrasos, 
        "Ishikawa_2_Final.png"
    )
    
    criar_ishikawa_final(
        "Falta de Padronização: Dificuldade de auditoria e fiscalização", 
        causas_padronizacao, 
        "Ishikawa_3_Final.png"
    )
    
    print("Concluído!")