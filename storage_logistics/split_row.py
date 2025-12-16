def split_row(nodes,y_top,y_bottom,spacing=1.5,x_shift=0):
    half=len(nodes)//2
    pos={}

    for i,node in enumerate(nodes):
        if i<half:
            x=i*spacing
            y=y_top
        else:
            x=(i-half)*spacing
            y=y_bottom
        pos[node]=(x+x_shift,y)
        
    return pos
