import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.5272e-02)
mat.add_nuclide('Pu240', 6.4479e-04)
mat.add_element('Ga', 2.0946e-03)
mat.add_element('Fe', 1.5659e-04)
mat.add_element('C', 2.9123e-04)
mat.add_element('Ni', 4.1459e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6826e-02)
mat.add_nuclide('Pu240', 6.7320e-04)
mat.add_element('Ga', 2.2000e-03)
mat.add_element('Fe', 1.4714e-04)
mat.add_element('C', 3.0406e-04)
mat.add_element('Ni', 1.5722e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6579e-02)
mat.add_nuclide('Pu240', 6.6875e-04)
mat.add_element('Ga', 2.2114e-03)
mat.add_element('Fe', 1.2992e-04)
mat.add_element('C', 3.0205e-04)
mat.add_element('Ni', 1.9330e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6512e-02)
mat.add_nuclide('Pu240', 6.6739e-04)
mat.add_element('Ga', 2.1940e-03)
mat.add_element('Fe', 1.2966e-04)
mat.add_element('C', 2.2608e-04)
mat.add_element('Ni', 2.3056e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6576e-02)
mat.add_nuclide('Pu240', 6.6878e-04)
mat.add_element('Ga', 2.2115e-03)
mat.add_element('Fe', 1.4617e-04)
mat.add_element('C', 3.0206e-04)
mat.add_element('Ni', 1.8631e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Steel reflector 1"
mat.set_density('sum')
mat.add_element('Fe', 7.9416e-02)
mat.add_element('C', 1.1269e-03)
mat.add_element('Si', 1.6065e-04)
mat.add_element('Cr', 2.6032e-04)
mat.add_element('Mn', 3.2850e-04)
mat.add_element('Ni', 2.3063e-04)
mat.add_element('Cu', 2.1300e-04)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Steel reflector 2"
mat.set_density('sum')
mat.add_element('Fe', 7.8919e-02)
mat.add_element('C', 1.1199e-03)
mat.add_element('Si', 1.5964e-04)
mat.add_element('Cr', 2.5869e-04)
mat.add_element('Mn', 3.2645e-04)
mat.add_element('Ni', 2.2918e-04)
mat.add_element('Cu', 2.1167e-04)
mats.append(mat)

mats.export_to_xml()
