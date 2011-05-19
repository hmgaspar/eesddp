import matplotlib.pyplot

import era
import run
import numpy


initial_year = 2011  


def Plot():
    num_era = len(era.output_era)
    
    PlotEraPro(run.output_vessel,num_era)
    for c,p in era.output_era:
          PlotEra(c,p)
    matplotlib.pyplot.show()

def PlotEraPro(out_ves,num_era):

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111)
        
    k_count = 0
    k_ini = 0
    k_color = 0.1
    nom_era = []
    for i in range(len(out_ves)/num_era):
        for k in range(num_era):
            ax.bar(k+k_ini,out_ves[k+k_count][4], width=0.7, bottom = 0, color=(k_color,0.68,1-k_color))
            k_color = k/float(num_era)
            ax.text(k+k_ini+0.35, out_ves[k+k_count][4]-0.5, out_ves[k+k_count][4], verticalalignment='center', color="black", size=10, weight = "bold")
        k_count = k_count + num_era
        k_ini = k_count + 0.5+i*0.5
        print k_count, k_ini
        ax.annotate(out_ves[i*num_era][0], xy=(k_ini-2, -0.7))
    
    ind_design = numpy.arange(0)
                       
    ax.set_title('Profit per Vessel')
    ax.set_xlabel('Designs')  
    ax.set_ylabel('Profit')
    ax.set_xticks(ind_design)
#   ax.set_yticklabels(c_names)
#    ax.grid(True)

def PlotEra(c,p):
  print '='*50
    #  print p
    #print c

  fig = matplotlib.pyplot.figure()
  ax = fig.add_subplot(111)
  posi = 10
  c_names = []
  c_pos = []
  for k in c:
    div_col = 1/float(len(c_pos)+1)
    ax.broken_barh([ (c[k]['start'], c[k]['duration']) ] , (posi+3, 5), 
                   facecolors=c[k]['color'])
    ax.broken_barh([ (c[k]['start'], c[k]['revenue']/2.0) ] , (posi, 2), 
                       facecolors=(0.76,0.92,0.77))
    ax.broken_barh([ (c[k]['start'], c[k]['complex']/2.0) ] , (posi-3, 2), 
                     facecolors=(0.92,0.91,0.76))
    ax.text(c[k]['start']-0.7, posi+5, "d: "+str(c[k]['duration']) , verticalalignment='center', color="black", size=10, weight = "bold")
    ax.text(c[k]['start']-0.7, posi, "r: "+str(c[k]['revenue']) , verticalalignment='center', color="black", size=10, weight = "bold")
    ax.text(c[k]['start']-0.7, posi-3, "c: "+str(c[k]['complex']) , verticalalignment='center', color="black", size=10, weight = "bold")

      
    c_pos.append(posi+5)
    posi = posi + 13
    c_names.append(k)
  
  epocas = set()
  for b,e,_,p1 in era.output_epoca:
    epocas.add(e)
    #  print len(epocas), p
  for i,e in enumerate(sorted(epocas)):
    ax.axvline(e+initial_year, color=(1,0,0))
    if i == 0:
       nome = "initial"
    else:
      nome = ','.join(x or "normal" for x in p[:i])
    ax.annotate(nome, xy=(e+initial_year, 13),  xycoords='data',
                xytext=(-75, -10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="angle3,angleA=0,angleB=90"),)

  ax.set_ylim(5,posi)
                
  ax.set_xlim(initial_year-2,era.era_size+initial_year+2)
#  print p
  ax.set_title('Era %s'%(p))
  ax.set_xlabel('Years')
  ax.set_yticks(c_pos)
  ax.set_yticklabels(c_names)
  ax.grid(True)
