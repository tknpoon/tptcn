USE secmaster;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkCertAfD' as `symbol`, `date`, 
 `CertIndebtAfterDisc` as `open`,
 `CertIndebtAfterDisc` as `high`, 
 `CertIndebtAfterDisc` as `low`, 
 `CertIndebtAfterDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkCertB4D' as `symbol`, `date`, 
 `CertIndebtBeforeDisc` as `open`,
 `CertIndebtBeforeDisc` as `high`, 
 `CertIndebtBeforeDisc` as `low`, 
 `CertIndebtBeforeDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkGovtAfD' as `symbol`, `date`, 
 `GovtCirAfterDisc` as `open`,
 `GovtCirAfterDisc` as `high`, 
 `GovtCirAfterDisc` as `low`, 
 `GovtCirAfterDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkGovtB4D' as `symbol`, `date`, 
 `GovtCirBeforeDisc` as `open`,
 `GovtCirBeforeDisc` as `high`, 
 `GovtCirBeforeDisc` as `low`, 
 `GovtCirBeforeDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkCAggAfD' as `symbol`, `date`, 
 `CloseAggBalAfterDisc` as `open`,
 `CloseAggBalAfterDisc` as `high`, 
 `CloseAggBalAfterDisc` as `low`, 
 `CloseAggBalAfterDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkCAggB4D' as `symbol`, `date`, 
 `CloseAggBalBeforeDisc` as `open`,
 `CloseAggBalBeforeDisc` as `high`, 
 `CloseAggBalBeforeDisc` as `low`, 
 `CloseAggBalBeforeDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkOsEFAfD' as `symbol`, `date`, 
 `OutstandEFNAfterDisc` as `open`,
 `OutstandEFNAfterDisc` as `high`, 
 `OutstandEFNAfterDisc` as `low`, 
 `OutstandEFNAfterDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkOsEFB4D' as `symbol`, `date`, 
 `OutstandEFNBeforeDisc` as `open`,
 `OutstandEFNBeforeDisc` as `high`, 
 `OutstandEFNBeforeDisc` as `low`, 
 `OutstandEFNBeforeDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkOsBKAfD' as `symbol`, `date`, 
 `OutstandEFNBankAfterDisc` as `open`,
 `OutstandEFNBankAfterDisc` as `high`, 
 `OutstandEFNBankAfterDisc` as `low`, 
 `OutstandEFNBankAfterDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkOsBKB4D' as `symbol`, `date`, 
 `OutstandEFNBankBeforeDisc` as `open`,
 `OutstandEFNBankBeforeDisc` as `high`, 
 `OutstandEFNBankBeforeDisc` as `low`, 
 `OutstandEFNBankBeforeDisc` as `close`, 
 0 as `volume`
FROM `tHKMA`;

REPLACE INTO tDailyPrice (`symbol`,`date`,`open`,`high`,`low`,`close`,`volume`)
SELECT 'hkTotal' as `symbol`, `date`, 
 `Total` as `open`,
 `Total` as `high`, 
 `Total` as `low`, 
 `Total` as `close`, 
 0 as `volume`
FROM `tHKMA`;



