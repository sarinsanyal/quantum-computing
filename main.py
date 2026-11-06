from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)
qc.h(0)
print(qc.draw())
print(Statevector(qc).probabilities_dict())  # {'1': 1.0}