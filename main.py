from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram
from qiskit_textbook.widgets import binary_widget
binary_widget(nbits=5)

#quantum circuit
qc_output = QuantumCircuit(8)
qc_output.measure_all()
qc_output.draw(initial_state=True)
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_output).result()
counts = result.get_counts()
plot_histogram(counts)

# adder circuit
qc_encode = QuantumCircuit(8)
qc_encode.x(7)
qc_encode.draw()
qc_encode.measure_all()
qc_encode.draw()

sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_encode).result()
counts = result.get_counts()
plot_histogram(counts)
qc_encode = QuantumCircuit(8)
qc_encode.x(1)
qc_encode.x(5)

qc_encode.draw()

# controlled-not gate
qc_cnot = QuantumCircuit(2)
qc_cnot.cx(0,1)
qc_cnot.draw()

qc = QuantumCircuit(2,2)
qc.x(0)
qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)
qc.draw()

# half adder
qc_ha = QuantumCircuit(4,2)
qc_ha.x(0)
qc_ha.x(1)
qc_ha.barrier()

qc_ha.cx(0,2)
qc_ha.cx(1,2)
qc_ha.barrier()

qc_ha.measure(2,0)
qc_ha.measure(3,1)

qc_ha.draw()

# toffoli
qc_ha = QuantumCircuit(4,2)

qc_ha.x(0)
qc_ha.x(1)
qc_ha.barrier()

qc_ha.cx(0,2)
qc_ha.cx(1,2)

qc_ha.ccx(0,1,3)
qc_ha.barrier()

qc_ha.measure(2,0)
qc_ha.measure(3,1)

qc_ha.draw()

# 1+1
qobj = assemble(qc_ha)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)