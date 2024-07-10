package model

type Book struct {
	Id    int64  `gorm:"primary_key" json:"id"`
	Name  string `gorm:"not null" json:"Name" binding:"required"`
	Desc  string `json:"desc"`
	Users []User `gorm:"many2many:book_users;"`
}

func (Book) TableName() string {
	return "book"
}
