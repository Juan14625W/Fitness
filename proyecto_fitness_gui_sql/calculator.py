# calculator.py
class CalculadoraFitness:
    
    @staticmethod
    def calcular_peso_ideal(usuario):
        """Fórmula del Dr. Miller para Peso Ideal (IBW)"""
        if usuario.genero == 'hombre':
            return 56.2 + 1.41 * ((usuario.altura_cm / 2.54) - 60)
        else:
            return 53.1 + 1.36 * ((usuario.altura_cm / 2.54) - 60)

    @staticmethod
    def calcular_calorias_quemadas(peso_kg, tiempo_min, met):
        """Fórmula para el cálculo de calorías quemadas."""
        return (tiempo_min * met * peso_kg) / 200

    @staticmethod
    def calcular_imc(peso_kg, altura_cm):
        """Cálculo del Índice de Masa Corporal"""
        altura_m = altura_cm / 100.0
        return peso_kg / (altura_m ** 2)

    @classmethod
    def calcular_porcentaje_grasa(cls, usuario):
        """Cálculo del Porcentaje de Grasa Corporal (%GC)"""
        imc = cls.calcular_imc(usuario.peso_kg, usuario.altura_cm)
        if usuario.genero == 'hombre':
            return 1.20 * imc + 0.23 * usuario.edad - 16.2
        else:
            return 1.20 * imc + 0.23 * usuario.edad - 5.4

    @staticmethod
    def calcular_tmb(usuario):
        """Cálculo de la Tasa Metabólica Basal (TMB)"""
        p = usuario.peso_kg
        e = usuario.edad
        a = usuario.altura_cm
        if usuario.genero == 'hombre':
            return 13.397 * p + 4.799 * e - 5.677 * a + 88.362
        else:
            return 9.247 * p + 3.098 * e - 4.330 * a + 447.593
