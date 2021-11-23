import { Entity, Column, PrimaryColumn } from 'typeorm'

@Entity()
export class User {
  @PrimaryColumn({ type: 'varchar', length: 20 })
  userId: string

  @Column({ type: 'varchar', length: 320 })
  email: string

  @Column({ type: 'varchar', length: 64 })
  password: string

  @Column({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP', nullable: false })
  creation: string
}
