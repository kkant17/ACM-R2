from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

qc = QuantumCircuit(1)

initial_state = [0,1]
qc.initialize(initial_state, 0)
qc.draw()

sim = Aer.get_backend('aer_simulator')

qc = QuantumCircuit(1)
initial_state = [0,1]
qc.initialize(initial_state, 0)
qc.save_statevector()
qobj = assemble(qc)
result = sim.run(qobj).result()

out_state = result.get_statevector()
print(out_state)

qc.measure_all()
qc.draw()
qobj = assemble(qc)
result = sim.run(qobj).result()
counts = result.get_counts()
plot_histogram(counts)

initial_state = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>

qc = QuantumCircuit(1)
qc.initialize(initial_state, 0)
qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
print(state)

qobj = assemble(qc)
results = sim.run(qobj).result().get_counts()
plot_histogram(results)

#implications
vector = [1,1]
qc.initialize(vector, 0)

# observer effect
qc = QuantumCircuit(1) # We are redefining qc
initial_state = [0.+1.j/sqrt(2),1/sqrt(2)+0.j]
qc.initialize(initial_state, 0)
qc.draw()

qc.save_statevector()
result = sim.run(assemble(qc)).result()
state = result.get_statevector()
print("Qubit State = " + str(state))
qc = QuantumCircuit(1)
initial_state = [0.+1.j/sqrt(2),1/sqrt(2)+0.j]
qc.initialize(initial_state, 0)
qc.measure_all()
qc.save_statevector()
qc.draw()

qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
print("State of Measured Qubit = " + str(state))

# bloch sphere demo
from qiskit.visualization import plot_bloch_vector
coords = [1,pi/2,0]  # [Radius, Theta, Phi]
plot_bloch_vector(coords, coord_type='spherical')