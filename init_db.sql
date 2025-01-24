create table external_feed_read (
                                    id int(11) not null,
                                    last_time datetime(6) not null,
                                    last_zone_id bigint(20) not null,
                                    last_highest_order bigint(20) not null,
                                    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_swedish_ci;

insert into external_feed_read (id, last_time, last_zone_id, last_highest_order)
values (1, '2025-01-23', 430365, 4000000000);

create table improved_feed_item (
                                    id UUID not null,
                                    order_number bigint(20) not null,
                                    takeover_time datetime(6) not null,
                                    original_takeover JSON not null,
                                    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_swedish_ci;

create index index_feed_order on improved_feed_item (order_number);
create index index_takeover_time on improved_feed_item (takeover_time);
