create table external_feed_read (
                                    id int(11) not null,
                                    last_time datetime(6) not null,
                                    last_zone_id bigint(20) not null,
                                    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_swedish_ci;

insert into external_feed_read (id, last_time, last_zone_id)
values (1, '2025-01-23', 430365);

create table improved_takeover_feed_item (
                                    zone_id bigint(20) not null,
                                    takeover_time datetime(6) not null,
                                    original_takeover JSON not null,
                                    primary key (takeover_time, zone_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_swedish_ci;

create table improved_zone_feed_item (
                                    zone_id bigint(20) not null,
                                    zone_created datetime(6) not null,
                                    original_zone JSON not null,
                                    primary key (zone_created, zone_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_swedish_ci;
