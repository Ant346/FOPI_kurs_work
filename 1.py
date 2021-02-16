# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math as m

a=2*1e-3
δ=1.5*1e-3
Dδ=25*1e-3
h=6*1e-3
Bδ=0.4
Dm=Dδ-a
k=0.3
μ0=m.pi*4*1e-7

Sm=m.pi*Dm**2/4
Sδ=h*m.pi*Dδ
Sm_Sδ=Sm/Sδ
Bm=Bδ*Sm_Sδ*(1+k)
Bm=1.05
print(' Sm= %.3e\n' %Sm,'Sδ= %.3e\n' %Sδ,'Sm/Sδ= %.3e\n' %Sm_Sδ,'Bm= %.3e\n' %Bm)

Hm=75*1e3
Bm_Hm=Bm/Hm
Lm=Bm_Hm*(δ/(μ0*(1+k)))*Sm_Sδ

print(' Lm= %.3e\n' %Lm,'Dm= %.3e\n' %Dm)
print(' Bm_Hm= %.3e\n' %Bm_Hm)


# %%
koeff=Bm/0.45
Dm_opt=Dm*koeff
print('Dm_opt= %.3e\n' %Dm_opt)


# %%
Dm=Dm_opt

Sm=m.pi*Dm**2/4
Sδ=h*m.pi*Dδ
Sm_Sδ=Sm/Sδ
Bm=Bδ*Sm_Sδ*(1+k)
print(' Sm= %.3e\n' %Sm,'Sδ= %.3e\n' %Sδ,'Sm/Sδ= %.3e\n' %Sm_Sδ,'Bm= %.3e\n' %Bm)

Hm=95*1e3
Bm_Hm=Bm/Hm
Lm=Bm_Hm*(δ/(μ0*(1+k)))*Sm_Sδ

print(' Lm= %.3e\n' %Lm,'Dm= %.3e\n' %Dm)


# %%
Bm=1.05
Dm2=m.sqrt((Bm*(1+k)*Sm)/(Bδ*m.pi))
Dm2*1e3
Lm=Bm_Hm*(δ/(μ0*(1+k)))*Sm_Sδ


# %%



