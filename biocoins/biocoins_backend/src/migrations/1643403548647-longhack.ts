import {MigrationInterface, QueryRunner} from "typeorm";

export class longhack1643403548647 implements MigrationInterface {
    name = 'longhack1643403548647'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TABLE "active_session" ("id" varchar PRIMARY KEY NOT NULL, "token" text NOT NULL, "userId" text NOT NULL, "date" datetime NOT NULL DEFAULT (CURRENT_TIMESTAMP))`);
        await queryRunner.query(`CREATE TABLE "user" ("id" varchar PRIMARY KEY NOT NULL, "username" text NOT NULL, "email" text NOT NULL, "password" text NOT NULL, "date" datetime NOT NULL DEFAULT (CURRENT_TIMESTAMP))`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`DROP TABLE "user"`);
        await queryRunner.query(`DROP TABLE "active_session"`);
    }

}
