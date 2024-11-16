// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.1
// 	protoc        v5.28.2
// source: proto/leagues.proto

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

type CreateLeagueRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *CreateLeagueRequest) Reset() {
	*x = CreateLeagueRequest{}
	mi := &file_proto_leagues_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateLeagueRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateLeagueRequest) ProtoMessage() {}

func (x *CreateLeagueRequest) ProtoReflect() protoreflect.Message {
	mi := &file_proto_leagues_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateLeagueRequest.ProtoReflect.Descriptor instead.
func (*CreateLeagueRequest) Descriptor() ([]byte, []int) {
	return file_proto_leagues_proto_rawDescGZIP(), []int{0}
}

func (x *CreateLeagueRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type LeagueId struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *LeagueId) Reset() {
	*x = LeagueId{}
	mi := &file_proto_leagues_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *LeagueId) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LeagueId) ProtoMessage() {}

func (x *LeagueId) ProtoReflect() protoreflect.Message {
	mi := &file_proto_leagues_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LeagueId.ProtoReflect.Descriptor instead.
func (*LeagueId) Descriptor() ([]byte, []int) {
	return file_proto_leagues_proto_rawDescGZIP(), []int{1}
}

func (x *LeagueId) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

type GetLeagueResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id   int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *GetLeagueResponse) Reset() {
	*x = GetLeagueResponse{}
	mi := &file_proto_leagues_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetLeagueResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLeagueResponse) ProtoMessage() {}

func (x *GetLeagueResponse) ProtoReflect() protoreflect.Message {
	mi := &file_proto_leagues_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLeagueResponse.ProtoReflect.Descriptor instead.
func (*GetLeagueResponse) Descriptor() ([]byte, []int) {
	return file_proto_leagues_proto_rawDescGZIP(), []int{2}
}

func (x *GetLeagueResponse) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *GetLeagueResponse) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type UpdateLeagueRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id   int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *UpdateLeagueRequest) Reset() {
	*x = UpdateLeagueRequest{}
	mi := &file_proto_leagues_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdateLeagueRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateLeagueRequest) ProtoMessage() {}

func (x *UpdateLeagueRequest) ProtoReflect() protoreflect.Message {
	mi := &file_proto_leagues_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateLeagueRequest.ProtoReflect.Descriptor instead.
func (*UpdateLeagueRequest) Descriptor() ([]byte, []int) {
	return file_proto_leagues_proto_rawDescGZIP(), []int{3}
}

func (x *UpdateLeagueRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *UpdateLeagueRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

var File_proto_leagues_proto protoreflect.FileDescriptor

var file_proto_leagues_proto_rawDesc = []byte{
	0x0a, 0x13, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x6c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x73, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x05, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d,
	0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x29, 0x0a, 0x13, 0x43, 0x72, 0x65,
	0x61, 0x74, 0x65, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x22, 0x1a, 0x0a, 0x08, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x49, 0x64,
	0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64,
	0x22, 0x37, 0x0a, 0x11, 0x47, 0x65, 0x74, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0x39, 0x0a, 0x13, 0x55, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64,
	0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x32, 0x82, 0x02, 0x0a, 0x0e, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x73,
	0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x3b, 0x0a, 0x0c, 0x43, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x12, 0x1a, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e,
	0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x0f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x4c, 0x65, 0x61, 0x67,
	0x75, 0x65, 0x49, 0x64, 0x12, 0x36, 0x0a, 0x09, 0x47, 0x65, 0x74, 0x4c, 0x65, 0x61, 0x67, 0x75,
	0x65, 0x12, 0x0f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65,
	0x49, 0x64, 0x1a, 0x18, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x65, 0x74, 0x4c, 0x65,
	0x61, 0x67, 0x75, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x42, 0x0a, 0x0c,
	0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x12, 0x1a, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x4c, 0x65, 0x61, 0x67, 0x75,
	0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79,
	0x12, 0x37, 0x0a, 0x0c, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65,
	0x12, 0x0f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x4c, 0x65, 0x61, 0x67, 0x75, 0x65, 0x49,
	0x64, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x42, 0x45, 0x5a, 0x43, 0x67, 0x69, 0x74,
	0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x6d, 0x69, 0x63, 0x68, 0x61, 0x65, 0x6c, 0x68,
	0x79, 0x69, 0x2f, 0x62, 0x61, 0x73, 0x65, 0x62, 0x61, 0x6c, 0x6c, 0x2d, 0x6c, 0x65, 0x61, 0x67,
	0x75, 0x65, 0x2d, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x2d, 0x73, 0x79,
	0x73, 0x74, 0x65, 0x6d, 0x2f, 0x67, 0x61, 0x6d, 0x65, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_proto_leagues_proto_rawDescOnce sync.Once
	file_proto_leagues_proto_rawDescData = file_proto_leagues_proto_rawDesc
)

func file_proto_leagues_proto_rawDescGZIP() []byte {
	file_proto_leagues_proto_rawDescOnce.Do(func() {
		file_proto_leagues_proto_rawDescData = protoimpl.X.CompressGZIP(file_proto_leagues_proto_rawDescData)
	})
	return file_proto_leagues_proto_rawDescData
}

var file_proto_leagues_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_proto_leagues_proto_goTypes = []any{
	(*CreateLeagueRequest)(nil), // 0: proto.CreateLeagueRequest
	(*LeagueId)(nil),            // 1: proto.LeagueId
	(*GetLeagueResponse)(nil),   // 2: proto.GetLeagueResponse
	(*UpdateLeagueRequest)(nil), // 3: proto.UpdateLeagueRequest
	(*emptypb.Empty)(nil),       // 4: google.protobuf.Empty
}
var file_proto_leagues_proto_depIdxs = []int32{
	0, // 0: proto.LeaguesService.CreateLeague:input_type -> proto.CreateLeagueRequest
	1, // 1: proto.LeaguesService.GetLeague:input_type -> proto.LeagueId
	3, // 2: proto.LeaguesService.UpdateLeague:input_type -> proto.UpdateLeagueRequest
	1, // 3: proto.LeaguesService.DeleteLeague:input_type -> proto.LeagueId
	1, // 4: proto.LeaguesService.CreateLeague:output_type -> proto.LeagueId
	2, // 5: proto.LeaguesService.GetLeague:output_type -> proto.GetLeagueResponse
	4, // 6: proto.LeaguesService.UpdateLeague:output_type -> google.protobuf.Empty
	4, // 7: proto.LeaguesService.DeleteLeague:output_type -> google.protobuf.Empty
	4, // [4:8] is the sub-list for method output_type
	0, // [0:4] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_proto_leagues_proto_init() }
func file_proto_leagues_proto_init() {
	if File_proto_leagues_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_proto_leagues_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_proto_leagues_proto_goTypes,
		DependencyIndexes: file_proto_leagues_proto_depIdxs,
		MessageInfos:      file_proto_leagues_proto_msgTypes,
	}.Build()
	File_proto_leagues_proto = out.File
	file_proto_leagues_proto_rawDesc = nil
	file_proto_leagues_proto_goTypes = nil
	file_proto_leagues_proto_depIdxs = nil
}
