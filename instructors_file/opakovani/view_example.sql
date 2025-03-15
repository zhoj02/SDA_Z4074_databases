
CREATE VIEW soucasni_zamestnanci_v_praze AS
SELECT * FROM zamestnanci
WHERE pobocka = 'Praha' and is_active=True

SELECT pobocka_nazev_cu as muj_nazev from soucasni_zamestnanci_v_praze
WHERE email LIKE '%zhouf'

