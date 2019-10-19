import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranium Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 7.1630e-07)
mat.add_nuclide('U235', 6.3904e-05)
mat.add_nuclide('U236', 1.8438e-07)
mat.add_nuclide('U238', 3.7311e-06)
mat.add_nuclide('N14', 2.3909e-04)
mat.add_nuclide('B10', 2.0725e-06)
mat.add_nuclide('B11', 8.3421e-06)
mat.add_nuclide('O16', 3.3713e-02)
mat.add_nuclide('O17', 1.2816e-05)
mat.add_nuclide('H1', 6.5815e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Type 1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9699e-02)
mat.add_element('Si', 5.5202e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mats.export_to_xml()
