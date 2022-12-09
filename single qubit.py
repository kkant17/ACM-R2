from qiskit import QuantumCircuit, assemble, Aer
from math import pi, sqrt
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_textbook.widgets import gate_demo
gate_demo(gates='pauli')
sim = Aer.get_backend('aer_simulator')

qc = QuantumCircuit(1)
qc.x(0)
qc.draw()

qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
plot_bloch_multivector(state)

qc.y(0)
qc.z(0)
qc.draw()

# Hardamard gate
from qiskit_textbook.widgets import gate_demo
gate_demo(gates='pauli+h')

# Create the X-measurement function:


def x_measurement(qc, qubit, cbit):
    """Measure 'qubit' in the X-basis, and store the result in 'cbit'"""
    qc.h(qubit)
    qc.measure(qubit, cbit)
    return qc


initial_state = [1/sqrt(2), -1/sqrt(2)]
qc = QuantumCircuit(1,1)
qc.initialize(initial_state, 0)
x_measurement(qc, 0, 0)  # measure qubit 0 to classical bit 0
qc.draw()


qobj = assemble(qc)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)

# P gate
from qiskit_textbook.widgets import gate_demo
gate_demo(gates='pauli+h+p')
qc = QuantumCircuit(1)
qc.p(pi/4, 0)
qc.draw()

# S-gate
qc = QuantumCircuit(1)
qc.s(0)
qc.sdg(0)
qc.draw()

# T gate
qc = QuantumCircuit(1)
qc.t(0)
qc.tdg(0)
qc.draw()