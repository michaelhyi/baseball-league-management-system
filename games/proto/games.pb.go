// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.1
// 	protoc        v5.28.2
// source: proto/games.proto

package proto

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type CreateGameRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	HomeTeamId    int32  `protobuf:"varint,1,opt,name=homeTeamId,proto3" json:"homeTeamId,omitempty"`
	AwayTeamId    int32  `protobuf:"varint,2,opt,name=awayTeamId,proto3" json:"awayTeamId,omitempty"`
	HomeTeamScore int32  `protobuf:"varint,3,opt,name=homeTeamScore,proto3" json:"homeTeamScore,omitempty"`
	AwayTeamScore int32  `protobuf:"varint,4,opt,name=awayTeamScore,proto3" json:"awayTeamScore,omitempty"`
	Date          string `protobuf:"bytes,5,opt,name=date,proto3" json:"date,omitempty"`
	Location      string `protobuf:"bytes,6,opt,name=location,proto3" json:"location,omitempty"`
}

func (x *CreateGameRequest) Reset() {
	*x = CreateGameRequest{}
	mi := &file_proto_games_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateGameRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateGameRequest) ProtoMessage() {}

func (x *CreateGameRequest) ProtoReflect() protoreflect.Message {
	mi := &file_proto_games_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateGameRequest.ProtoReflect.Descriptor instead.
func (*CreateGameRequest) Descriptor() ([]byte, []int) {
	return file_proto_games_proto_rawDescGZIP(), []int{0}
}

func (x *CreateGameRequest) GetHomeTeamId() int32 {
	if x != nil {
		return x.HomeTeamId
	}
	return 0
}

func (x *CreateGameRequest) GetAwayTeamId() int32 {
	if x != nil {
		return x.AwayTeamId
	}
	return 0
}

func (x *CreateGameRequest) GetHomeTeamScore() int32 {
	if x != nil {
		return x.HomeTeamScore
	}
	return 0
}

func (x *CreateGameRequest) GetAwayTeamScore() int32 {
	if x != nil {
		return x.AwayTeamScore
	}
	return 0
}

func (x *CreateGameRequest) GetDate() string {
	if x != nil {
		return x.Date
	}
	return ""
}

func (x *CreateGameRequest) GetLocation() string {
	if x != nil {
		return x.Location
	}
	return ""
}

type UpdateGameRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id            int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	HomeTeamId    int32  `protobuf:"varint,2,opt,name=homeTeamId,proto3" json:"homeTeamId,omitempty"`
	AwayTeamId    int32  `protobuf:"varint,3,opt,name=awayTeamId,proto3" json:"awayTeamId,omitempty"`
	HomeTeamScore int32  `protobuf:"varint,4,opt,name=homeTeamScore,proto3" json:"homeTeamScore,omitempty"`
	AwayTeamScore int32  `protobuf:"varint,5,opt,name=awayTeamScore,proto3" json:"awayTeamScore,omitempty"`
	Date          string `protobuf:"bytes,6,opt,name=date,proto3" json:"date,omitempty"`
	Location      string `protobuf:"bytes,7,opt,name=location,proto3" json:"location,omitempty"`
}

func (x *UpdateGameRequest) Reset() {
	*x = UpdateGameRequest{}
	mi := &file_proto_games_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdateGameRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateGameRequest) ProtoMessage() {}

func (x *UpdateGameRequest) ProtoReflect() protoreflect.Message {
	mi := &file_proto_games_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateGameRequest.ProtoReflect.Descriptor instead.
func (*UpdateGameRequest) Descriptor() ([]byte, []int) {
	return file_proto_games_proto_rawDescGZIP(), []int{1}
}

func (x *UpdateGameRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *UpdateGameRequest) GetHomeTeamId() int32 {
	if x != nil {
		return x.HomeTeamId
	}
	return 0
}

func (x *UpdateGameRequest) GetAwayTeamId() int32 {
	if x != nil {
		return x.AwayTeamId
	}
	return 0
}

func (x *UpdateGameRequest) GetHomeTeamScore() int32 {
	if x != nil {
		return x.HomeTeamScore
	}
	return 0
}

func (x *UpdateGameRequest) GetAwayTeamScore() int32 {
	if x != nil {
		return x.AwayTeamScore
	}
	return 0
}

func (x *UpdateGameRequest) GetDate() string {
	if x != nil {
		return x.Date
	}
	return ""
}

func (x *UpdateGameRequest) GetLocation() string {
	if x != nil {
		return x.Location
	}
	return ""
}

type GameId struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *GameId) Reset() {
	*x = GameId{}
	mi := &file_proto_games_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GameId) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GameId) ProtoMessage() {}

func (x *GameId) ProtoReflect() protoreflect.Message {
	mi := &file_proto_games_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GameId.ProtoReflect.Descriptor instead.
func (*GameId) Descriptor() ([]byte, []int) {
	return file_proto_games_proto_rawDescGZIP(), []int{2}
}

func (x *GameId) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

type GetGameResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id            int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	HomeTeamId    int32  `protobuf:"varint,2,opt,name=homeTeamId,proto3" json:"homeTeamId,omitempty"`
	AwayTeamId    int32  `protobuf:"varint,3,opt,name=awayTeamId,proto3" json:"awayTeamId,omitempty"`
	HomeTeamScore int32  `protobuf:"varint,4,opt,name=homeTeamScore,proto3" json:"homeTeamScore,omitempty"`
	AwayTeamScore int32  `protobuf:"varint,5,opt,name=awayTeamScore,proto3" json:"awayTeamScore,omitempty"`
	Date          string `protobuf:"bytes,6,opt,name=date,proto3" json:"date,omitempty"`
	Location      string `protobuf:"bytes,7,opt,name=location,proto3" json:"location,omitempty"`
	CreatedAt     string `protobuf:"bytes,8,opt,name=createdAt,proto3" json:"createdAt,omitempty"`
	UpdatedAt     string `protobuf:"bytes,9,opt,name=updatedAt,proto3" json:"updatedAt,omitempty"`
}

func (x *GetGameResponse) Reset() {
	*x = GetGameResponse{}
	mi := &file_proto_games_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetGameResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetGameResponse) ProtoMessage() {}

func (x *GetGameResponse) ProtoReflect() protoreflect.Message {
	mi := &file_proto_games_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetGameResponse.ProtoReflect.Descriptor instead.
func (*GetGameResponse) Descriptor() ([]byte, []int) {
	return file_proto_games_proto_rawDescGZIP(), []int{3}
}

func (x *GetGameResponse) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *GetGameResponse) GetHomeTeamId() int32 {
	if x != nil {
		return x.HomeTeamId
	}
	return 0
}

func (x *GetGameResponse) GetAwayTeamId() int32 {
	if x != nil {
		return x.AwayTeamId
	}
	return 0
}

func (x *GetGameResponse) GetHomeTeamScore() int32 {
	if x != nil {
		return x.HomeTeamScore
	}
	return 0
}

func (x *GetGameResponse) GetAwayTeamScore() int32 {
	if x != nil {
		return x.AwayTeamScore
	}
	return 0
}

func (x *GetGameResponse) GetDate() string {
	if x != nil {
		return x.Date
	}
	return ""
}

func (x *GetGameResponse) GetLocation() string {
	if x != nil {
		return x.Location
	}
	return ""
}

func (x *GetGameResponse) GetCreatedAt() string {
	if x != nil {
		return x.CreatedAt
	}
	return ""
}

func (x *GetGameResponse) GetUpdatedAt() string {
	if x != nil {
		return x.UpdatedAt
	}
	return ""
}

var File_proto_games_proto protoreflect.FileDescriptor

var file_proto_games_proto_rawDesc = []byte{
	0x0a, 0x11, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x67, 0x61, 0x6d, 0x65, 0x73, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x12, 0x05, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74,
	0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xcf, 0x01, 0x0a, 0x11, 0x43, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x47, 0x61, 0x6d, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1e, 0x0a,
	0x0a, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x05, 0x52, 0x0a, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x12, 0x1e, 0x0a,
	0x0a, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x05, 0x52, 0x0a, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x12, 0x24, 0x0a,
	0x0d, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x0d, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63,
	0x6f, 0x72, 0x65, 0x12, 0x24, 0x0a, 0x0d, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x53,
	0x63, 0x6f, 0x72, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0d, 0x61, 0x77, 0x61, 0x79,
	0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x64, 0x61, 0x74,
	0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x64, 0x61, 0x74, 0x65, 0x12, 0x1a, 0x0a,
	0x08, 0x6c, 0x6f, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x08, 0x6c, 0x6f, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0xdf, 0x01, 0x0a, 0x11, 0x55, 0x70,
	0x64, 0x61, 0x74, 0x65, 0x47, 0x61, 0x6d, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12,
	0x1e, 0x0a, 0x0a, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x05, 0x52, 0x0a, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x12,
	0x1e, 0x0a, 0x0a, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x05, 0x52, 0x0a, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x12,
	0x24, 0x0a, 0x0d, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0d, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d,
	0x53, 0x63, 0x6f, 0x72, 0x65, 0x12, 0x24, 0x0a, 0x0d, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61,
	0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0d, 0x61, 0x77,
	0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x64,
	0x61, 0x74, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x64, 0x61, 0x74, 0x65, 0x12,
	0x1a, 0x0a, 0x08, 0x6c, 0x6f, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x07, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x08, 0x6c, 0x6f, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x18, 0x0a, 0x06, 0x47,
	0x61, 0x6d, 0x65, 0x49, 0x64, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x05, 0x52, 0x02, 0x69, 0x64, 0x22, 0x99, 0x02, 0x0a, 0x0f, 0x47, 0x65, 0x74, 0x47, 0x61, 0x6d,
	0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x1e, 0x0a, 0x0a, 0x68, 0x6f, 0x6d,
	0x65, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x68,
	0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x12, 0x1e, 0x0a, 0x0a, 0x61, 0x77, 0x61,
	0x79, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x61,
	0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x49, 0x64, 0x12, 0x24, 0x0a, 0x0d, 0x68, 0x6f, 0x6d,
	0x65, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05,
	0x52, 0x0d, 0x68, 0x6f, 0x6d, 0x65, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65, 0x12,
	0x24, 0x0a, 0x0d, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d, 0x53, 0x63, 0x6f, 0x72, 0x65,
	0x18, 0x05, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0d, 0x61, 0x77, 0x61, 0x79, 0x54, 0x65, 0x61, 0x6d,
	0x53, 0x63, 0x6f, 0x72, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x65, 0x18, 0x06, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x04, 0x64, 0x61, 0x74, 0x65, 0x12, 0x1a, 0x0a, 0x08, 0x6c, 0x6f, 0x63,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6c, 0x6f, 0x63,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1c, 0x0a, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64,
	0x41, 0x74, 0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x64, 0x41, 0x74, 0x12, 0x1c, 0x0a, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74,
	0x18, 0x09, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41,
	0x74, 0x32, 0xf4, 0x01, 0x0a, 0x0c, 0x47, 0x61, 0x6d, 0x65, 0x73, 0x53, 0x65, 0x72, 0x76, 0x69,
	0x63, 0x65, 0x12, 0x37, 0x0a, 0x0a, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x47, 0x61, 0x6d, 0x65,
	0x12, 0x18, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x47,
	0x61, 0x6d, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0d, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x47, 0x61, 0x6d, 0x65, 0x49, 0x64, 0x22, 0x00, 0x12, 0x32, 0x0a, 0x07, 0x47,
	0x65, 0x74, 0x47, 0x61, 0x6d, 0x65, 0x12, 0x0d, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47,
	0x61, 0x6d, 0x65, 0x49, 0x64, 0x1a, 0x16, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x65,
	0x74, 0x47, 0x61, 0x6d, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x12,
	0x40, 0x0a, 0x0a, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x47, 0x61, 0x6d, 0x65, 0x12, 0x18, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x47, 0x61, 0x6d, 0x65,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x22,
	0x00, 0x12, 0x35, 0x0a, 0x0a, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x47, 0x61, 0x6d, 0x65, 0x12,
	0x0d, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x61, 0x6d, 0x65, 0x49, 0x64, 0x1a, 0x16,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x22, 0x00, 0x42, 0x45, 0x5a, 0x43, 0x67, 0x69, 0x74, 0x68,
	0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x6d, 0x69, 0x63, 0x68, 0x61, 0x65, 0x6c, 0x68, 0x79,
	0x69, 0x2f, 0x62, 0x61, 0x73, 0x65, 0x62, 0x61, 0x6c, 0x6c, 0x2d, 0x6c, 0x65, 0x61, 0x67, 0x75,
	0x65, 0x2d, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x2d, 0x73, 0x79, 0x73,
	0x74, 0x65, 0x6d, 0x2f, 0x67, 0x61, 0x6d, 0x65, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_proto_games_proto_rawDescOnce sync.Once
	file_proto_games_proto_rawDescData = file_proto_games_proto_rawDesc
)

func file_proto_games_proto_rawDescGZIP() []byte {
	file_proto_games_proto_rawDescOnce.Do(func() {
		file_proto_games_proto_rawDescData = protoimpl.X.CompressGZIP(file_proto_games_proto_rawDescData)
	})
	return file_proto_games_proto_rawDescData
}

var file_proto_games_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_proto_games_proto_goTypes = []any{
	(*CreateGameRequest)(nil), // 0: proto.CreateGameRequest
	(*UpdateGameRequest)(nil), // 1: proto.UpdateGameRequest
	(*GameId)(nil),            // 2: proto.GameId
	(*GetGameResponse)(nil),   // 3: proto.GetGameResponse
	(*emptypb.Empty)(nil),     // 4: google.protobuf.Empty
}
var file_proto_games_proto_depIdxs = []int32{
	0, // 0: proto.GamesService.CreateGame:input_type -> proto.CreateGameRequest
	2, // 1: proto.GamesService.GetGame:input_type -> proto.GameId
	1, // 2: proto.GamesService.UpdateGame:input_type -> proto.UpdateGameRequest
	2, // 3: proto.GamesService.DeleteGame:input_type -> proto.GameId
	2, // 4: proto.GamesService.CreateGame:output_type -> proto.GameId
	3, // 5: proto.GamesService.GetGame:output_type -> proto.GetGameResponse
	4, // 6: proto.GamesService.UpdateGame:output_type -> google.protobuf.Empty
	4, // 7: proto.GamesService.DeleteGame:output_type -> google.protobuf.Empty
	4, // [4:8] is the sub-list for method output_type
	0, // [0:4] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_proto_games_proto_init() }
func file_proto_games_proto_init() {
	if File_proto_games_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_proto_games_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_proto_games_proto_goTypes,
		DependencyIndexes: file_proto_games_proto_depIdxs,
		MessageInfos:      file_proto_games_proto_msgTypes,
	}.Build()
	File_proto_games_proto = out.File
	file_proto_games_proto_rawDesc = nil
	file_proto_games_proto_goTypes = nil
	file_proto_games_proto_depIdxs = nil
}
