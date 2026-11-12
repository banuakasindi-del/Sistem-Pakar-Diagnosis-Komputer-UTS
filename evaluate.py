from knowledge_base import RULES

# Lima skenario uji non-ML sesuai ketentuan UTS.
TESTS = [
    ("T1 - Daya", {"tidak_menyala", "lampu_indikator_mati"}, 
     "Masalah daya / PSU atau adaptor", "R01"),
    ("T2 - RAM", {"menyala_tanpa_tampilan", "bunyi_beep"}, 
     "RAM longgar atau bermasalah", "R02"),
    ("T3 - Display", {"komputer_menyala", "monitor_no_signal"}, 
     "Gangguan monitor atau kabel display", "R03"),
    ("T4 - Overheating", {"mati_mendadak", "kipas_bising_panas"}, 
     "Panas berlebih (overheating)", "R04"),
    ("T5 - Disk", {"boot_gagal", "pesan_disk_error"}, 
     "Penyimpanan HDD/SSD bermasalah", "R05"),
]

def infer(facts):
    results = []
    for rule in RULES:
        if set(rule["symptoms"]).issubset(facts):
            results.append(rule)
    return results

if __name__ == "__main__":
    print("EVALUASI SISTEM PAKAR - 5 SKENARIO")
    passed = 0
    for name, facts, expected, rule_id in TESTS:
        results = infer(facts)
        actual = [r["name"] for r in results]
        ok = expected in actual and any(r["id"] == rule_id for r in results)
        passed += int(ok)
        print(f"{name}: {'LULUS' if ok else 'GAGAL'}")
        print(f"  Diharapkan: {expected}")
        print(f"  Aktual: {', '.join(actual) 
                           if actual else 'Tidak ada diagnosis'}")
    print(f"\nHasil: {passed}/{len(TESTS)} 
    skenario lulus ({passed/len(TESTS)*100:.1f}%)")
