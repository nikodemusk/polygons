import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import numpy as np
plt.style.use("dark_background")
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams['font.family'] = 'serif'

xlimit = (-0.8, 0.8)
ylimit = (-0.8, 0.8)
x, y = 0, 0 # center
subpol = 100
nv = [3, 4, 8] # Number of vertices in each row
color = np.linspace(0, .9, subpol)
lineWidth = 0.75

showTextLabels = True
fontSize = 22

fig, ax = plt.subplots(3, 3, figsize=(20,20))
fig.set_dpi(100)

# Create row 0
row = 0
# Outer loop, 3 columns. Each columns consists of triangles turned
# in different angles.
for col in range(0, 3):
    rot = [0, 2, 40] # Rotation in each column
    
    # Inner loop, operates on one column. Creates the turned triangles
    # in different sizes.
    for j in range(0, subpol):
        polyParams = {'facecolor':'none',                                                                                 
          'edgecolor':[0.8, color[j], 0.1, 1/((j+2)**(0.1))],
          'linewidth':lineWidth,
          'radius': 1/((j+2)**0.4),
          'numVertices': nv[row],
          'xy': (x, y),
          'orientation': 0}
        
        rotationParams = {'degrees':j*rot[col]}
        textParams = {
                      'verticalalignment': 'center',
                      'horizontalalignment': 'center',
                      'fontsize': fontSize,
                      'transform': ax[row, col].transAxes}
        
        polygon = mpatches.RegularPolygon(**polyParams)
        transform = mpl.transforms.Affine2D().rotate_deg_around(x, y, **rotationParams)
        p = ax[row, col].add_patch(polygon)
        polygon.set_transform(transform+ax[row, col].transData)
        
    ax[row, col].set_aspect('equal')
    ax[row, col].axis('off')
    ax[row, col].set_xlim(xlimit)
    ax[row, col].set_ylim(ylimit)
    
    if showTextLabels:
        plt.text(0.5, 0.1, f'$n={nv[row]}$, $\\alpha = {rot[col]}^\degree$', **textParams)
        
    extent = ax[row, col].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    if showTextLabels:
        fig.savefig(f'polygon_{nv[row]}_{col}.png', bbox_inches=extent)
    else:
        fig.savefig(f'polygon_{nv[row]}_{col}.png', bbox_inches=extent)
        
# Create row 1
row = 1
# Outer loop, 3 columns. Each columns consists of triangles turned
# in different angles.
for col in range(0, 3):
    rot = [0, 2, 15] # Rotation in each column
    
    # Inner loop, operates on one column. Creates the turned triangles
    # in different sizes.
    for j in range(0, subpol):
        polyParams = {'facecolor':'none',                                                                                 
          'edgecolor':[0.2, 1, color[j], 1/((j+2)**(0.1))],
          'linewidth':lineWidth,
          'radius': 1/((j+2)**0.4),
          'numVertices': nv[row],
          'xy': (x, y),
          'orientation': 0}
        
        rotationParams = {'degrees':j*rot[col]}
        textParams = {
                      'verticalalignment': 'center',
                      'horizontalalignment': 'center',
                      'fontsize': fontSize,
                      'transform': ax[row, col].transAxes}
        
        polygon = mpatches.RegularPolygon(**polyParams)
        transform = mpl.transforms.Affine2D().rotate_deg_around(x, y, **rotationParams)
        p = ax[row, col].add_patch(polygon)
        polygon.set_transform(transform+ax[row, col].transData)
        
    ax[row, col].set_aspect('equal')
    ax[row, col].axis('off')
    ax[row, col].set_xlim(xlimit)
    ax[row, col].set_ylim(ylimit)
    
    if showTextLabels:
        ax[row, col].text(0.5, -0.025, f'$n={nv[row]}$, $\\alpha = {rot[col]}^\degree$', **textParams)

    extent = ax[row, col].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    if showTextLabels:
        fig.savefig(f'polygon_{nv[row]}_{col}.png', bbox_inches=extent.expanded(1.1, 1.2))
    else:
        fig.savefig(f'polygon_{nv[row]}_{col}.png', bbox_inches=extent)

# Create row 2
row = 2
# Outer loop, 3 columns. Each columns consists of triangles turned
# in different angles.
for col in range(0, 3):
    rot = [0, 2, 22.5] # Rotation in each column
    
    # Inner loop, operates on one column. Creates the turned triangles
    # in different sizes.
    for j in range(0, subpol):
        polyParams = {'facecolor':'none',                                                                                 
          'edgecolor':[color[j], 0.8, 0.9, 1/((j+2)**(0.1))],
          'linewidth':lineWidth,
          'radius': 1/((j+2)**0.4),
          'numVertices': nv[row],
          'xy': (x, y),
          'orientation': 0}
        
        rotationParams = {'degrees':j*rot[col]}
        textParams = {
                      'verticalalignment': 'center',
                      'horizontalalignment': 'center',
                      'fontsize': fontSize,
                      'transform': ax[row, col].transAxes}
        
        polygon = mpatches.RegularPolygon(**polyParams)
        transform = mpl.transforms.Affine2D().rotate_deg_around(x, y, **rotationParams)
        p = ax[row, col].add_patch(polygon)
        polygon.set_transform(transform+ax[row, col].transData)
        
    ax[row, col].set_aspect('equal')
    ax[row, col].axis('off')
    ax[row, col].set_xlim(xlimit)
    ax[row, col].set_ylim(ylimit)
    
    if showTextLabels:
        ax[row, col].text(0.5, -0.025, f'$n={nv[row]}$, $\\alpha = {rot[col]}^\degree$', **textParams)
    
    extent = ax[row, col].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    if showTextLabels:
        fig.savefig(f'polygon_{nv[row]}_{col}.png', bbox_inches=extent.expanded(1.1, 1.2))
    else:
        fig.savefig(f'polygon_{nv[row]}_{col}.png', bbox_inches=extent)

fig.savefig('full.png', bbox_inches='tight')
plt.show()
