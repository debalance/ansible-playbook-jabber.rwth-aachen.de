-- The following sql code is a modified excerpt from
-- /usr/share/doc/ejabberd/examples/mysql.sql.gz
-- because we only need the tables "archive" and "archive_prefs".

--
-- ejabberd, Copyright (C) 2002-2016   ProcessOne
--
-- This program is free software; you can redistribute it and/or
-- modify it under the terms of the GNU General Public License as
-- published by the Free Software Foundation; either version 2 of the
-- License, or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
-- General Public License for more details.
--
-- You should have received a copy of the GNU General Public License along
-- with this program; if not, write to the Free Software Foundation, Inc.,
-- 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
--

CREATE TABLE IF NOT EXISTS archive (
    username varchar(191) NOT NULL,
    timestamp BIGINT UNSIGNED NOT NULL,
    peer varchar(191) NOT NULL,
    bare_peer varchar(191) NOT NULL,
    xml text NOT NULL,
    txt text,
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
    kind varchar(10),
    nick varchar(191),
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE FULLTEXT INDEX i_text ON archive(txt);
CREATE INDEX i_username USING BTREE ON archive(username);
CREATE INDEX i_timestamp USING BTREE ON archive(timestamp);
CREATE INDEX i_peer USING BTREE ON archive(peer);
CREATE INDEX i_bare_peer USING BTREE ON archive(bare_peer);

CREATE TABLE IF NOT EXISTS archive_prefs (
    username varchar(191) NOT NULL PRIMARY KEY,
    def text NOT NULL,
    always text NOT NULL,
    never text NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
