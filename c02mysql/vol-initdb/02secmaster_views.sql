INSERT INTO `tVendor`(`name`) VALUES ("yahoo");
INSERT INTO `tVendor`(`name`) VALUES ("hkex");
INSERT INTO `tVendor`(`name`) VALUES ("hkma");

CREATE VIEW `vDaily` AS
  SELECT  d.symbol symbol,
    d.price_date date, 
    d.open_price open, d.high_price high, d.low_price low, d.close_price close, d.volume volume
  FROM    tDailyPrice d;  

