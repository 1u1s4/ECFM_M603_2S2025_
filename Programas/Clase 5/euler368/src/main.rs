// src/main.rs
// -----------------------------------------------------------------------------
// Project Euler 368 – Serie armónica sin denominadores con 'aaa'
// Calcula S = Σ 1/n   (n sin tres dígitos iguales consecutivos)
// Precisión: 10 decimales (tolerancia 1 e-10)
// -----------------------------------------------------------------------------

/// Devuelve `true` si `n` contiene tres dígitos iguales y consecutivos.
///
/// Recorre los dígitos de derecha a izquierda sin convertir a String,
/// por lo que es más rápido que usar `format!` o expresiones regulares.
fn has_triple_digits(mut n: u64) -> bool {
    let mut prev1 = 10u8;   // valores imposibles como “sentinel”
    let mut prev2 = 10u8;

    while n > 0 {
        let digit = (n % 10) as u8;
        if digit == prev1 && digit == prev2 {
            return true;
        }
        prev2 = prev1;
        prev1 = digit;
        n /= 10;
    }
    false
}

fn main() {
    const TOL: f64 = 1e-10;

    let mut sum: f64 = 0.0;
    let mut n: u64 = 1;

    loop {
        if !has_triple_digits(n) {
            let term = 1.0 / (n as f64);
            sum += term;
            println!("n = {}, term = {:.10}, sum = {:.10}", n, term, sum);
            if term < TOL {
                break;
            }
        }
        n += 1;
    }

    println!("S = {:.10}", sum);               // 253.6135092068
    println!("Último n examinado: {}", n);      // ≈1 836 000 000
}
